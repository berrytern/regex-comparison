# FFI trade-offs

<b>Short answer:</b>
You must know the trade-offs to decide…, So let's dive in on it.

## Overall overview
### When should Rust FFI be used over python:
- CPU bound tasks;</br>
Why: Rust’s compiler can optimize code and the machine code is faster than the python’s interpreter iteration over bytecode.
- low level memory control;

### When shouldn’t use FFI:
- Your code is fast enough;
- Your team cannot maintain the new language code;
<br>e.g. The extra memory overhead is not acceptable(rust side), “so why use python in the first place?”(‘-’);
Changing rust code requires compilation, it can slow your development speed.
- Your function is not used very often, the cost to rewrite it can not be worth it.
- Your function needs to parse input fields as copy and not as reference/zero-copy, maybe it can imply that Marshaling cost has been bigger than the processing gain of rust over python’s implementation.
### When you are using FFi wrongly:
- If your function is called inside a python’s loop/iteration and you can move the loop entirely to the rust side, avoiding the cost of call and of marshaling.
- If you can use a zero-copy approach instead, Ex([#pyclass]), python buffer protocol, 

### Notes: 
- Usage of FFI(pyo3) on async scenarios has some additional trade-offs(double eventloop, etc.).
<br>Check more in docs.
- Logging is normally handled by sending it from the rust side to python side.
<br>Check more in docs.

## Deeply Overview

What is important to know as base knowledge:

### Python World:
First of all, let's understand when python shines and when it does not.

#### Good when: 
- Code that was internally written in C or other compiled(low level language);<br>
e.g. List comprehension.
- base operations like sum, multi, sub, div, etc.
#### Slow when at:
- loops(for/while) and at computation tasks because of its interpreted nature

### FFI World:
#### Call cost:
#### base call cost:
  - python calling python: 50-100ns;
  - python calling c(cython): 30-60ns (Wrapper overhead)
  - python calling rust(PyO3) 100-150ns;<br>
#### Marshaling cost:
This depends entirely on whether the type is Native to Python (built-in C structures) or a Custom Class.

performance comparisons:

Here is the breakdown of how Rust extracts other common types from a `PyList`, ordered from Fastest to Slowest.

### 1. Integers, Floats, and Booleans (Fastest)

**Mechanism:** Direct C-Struct Read.

When you extract an `i32` or `f64`, PyO3 does **not** call any Python methods.

* **Python Representation:** An integer in Python is a C struct (`PyLongObject`) containing a reference count, a type pointer, and an array of "digits" (the number itself).
* **Rust Action:** PyO3 calls the C-API function `PyLong_AsLong`. This function looks directly at the `digits` field in memory and returns the raw number.

**Cost:**

* **Allocation:** Zero (scalars are copied by value, which is effectively free).
* **Speed:** Extremely fast. It is just a memory read + a few CPU cycles to check for overflow.

```rust
// Fast: Direct memory read from C-struct
let num: i32 = item.extract()?; 

```

### 2. Tuples (Very Fast)

**Mechanism:** Direct Pointer Array Access.

A Python tuple is structurally simpler than a list. It is an immutable array of pointers.

* **Rust Action:** If you extract a tuple `(i32, i32)`, PyO3 uses `PyTuple_GET_ITEM`. It grabs the pointer at index 0 and index 1 directly.
* **Recursion:** It then recursively performs the "Integer Extraction" (see #1) on those items.

**Cost:**

* **Allocation:** Zero (if extracting into a Rust tuple `(i32, i32)` which lives on the stack).
* **Speed:** Very fast. No dynamic lookups.

### 3. Rust-Defined Classes (`#[pyclass]`) (Lightning Fast)

**Mechanism:** Pointer Cast (Downcast).

This is a specific PyO3 "superpower." If the object in the list is a struct you defined in Rust and exposed to Python using `#[pyclass]`, PyO3 can "see through" the Python wrapper.

* **Rust Action:** PyO3 checks the type pointer. If it matches your Rust type, it literally casts the `PyObject` pointer back into a Rust reference `&MyStruct`.
* **Benefit:** You bypass **all** Python C-API overhead. You are reading fields of a Rust struct directly.

```rust
#[pyclass]
struct MyData { x: i32 }

// Inside your loop:
// This is NOT a conversion. It's a pointer cast.
// You get direct access to `x` in Rust memory.
let my_obj: &MyData = item.downcast::<MyData>()?.get();
println!("{}", my_obj.x);

```

### 4. Dictionaries (Medium - Variable)

**Mechanism:** Hash Table Lookup.

If you extract a `HashMap<String, i32>`, you pay a high price.

* **Rust Action:** PyO3 must iterate every key-value pair in the Python Dict, extract the key, extract the value, and **allocate** a new entry in a Rust `HashMap`.
* **Alternative (Better):** Use `Bound<'py, PyDict>`. This keeps the data in Python but gives you a handle. Accessing a value (`dict.get_item("key")`) calls the C-API `PyDict_GetItem`, which is a fast C-level hash lookup, but still slower than a direct array index.

### 5. Python-Defined Custom Classes (Slowest)

**Mechanism:** Attribute Lookup (Dictionary Search).

If you have a Python class defined in a `.py` file:

```python
class User:
    def __init__(self, age):
        self.age = age

```

And you try to extract this into a Rust struct:

* **Rust Action:** There is no standard C-struct for "User". The data lives inside a dynamic dictionary (`__dict__`).
* **The Process:**
1. PyO3 calls `PyObject_GetAttr(item, "age")`.
2. Python engine hashes the string "age".
3. Python engine searches the object's `__dict__`.
4. Returns the PyObject for the age.
5. Rust converts that PyObject to an `i32`.



**Cost:**

* **Speed:** Slow. You are paying for string hashing and dictionary lookups for *every single field* for *every single item* in the list.

---

### Summary of Costs

| Python Type | Rust Extraction | Mechanism | Speed |
| --- | --- | --- | --- |
| **Rust `#[pyclass]`** | `&MyStruct` | Pointer Cast (Raw Access) | 🚀 **Instant** |
| **Integer/Float** | `i32` / `f64` | C-Struct Field Read | ⚡ **Very Fast** |
| **Tuple** | `(i32, i32)` | Pointer Offset + Read | ⚡ **Very Fast** |
| **String** | `&str` | Pointer to UTF8 Buffer | ⚡ **Very Fast** |
| **List/Dict** | `Bound<'_, PyList>` | Reference to Object | ⚡ **Very Fast** |
| **List/Dict** | `Vec` / `HashMap` | **Deep Copy & Allocation** | 🐌 **Slow** |
| **Python Class** | Rust Struct | Attribute Lookup (HashMap) | 🐌 **Slowest** |

### The "Golden Rule" for Complex Types

If you are iterating over a list of complex objects:

1. **If you control the object:** Define it in Rust (`#[pyclass]`). This allows you to iterate millions of items with native Rust performance.
2. **If you don't control the object:** Do **not** try to convert it to a Rust struct inside the loop. Keep it as a `Bound<'py, PyAny>`. Only extract the *specific fields* you need (e.g., just `obj.getattr("id")?.extract::<i32>()?`). Don't decode the whole object if you don't have to.

### Specific comparisons
python's types need holds the GIL(PyAny, Pylist, PyDict, etc.)
rust's types does not need to hold the GIL(Vec, HashMap)  

#### list vs &bound<’py, Pylist>t vs Vec: 
##### Notes:
- memory layout differs.
- PyList can be used as copy or as reference(&bound<’py, Pylist>)
##### Vec:
- Lower memory overhead(can allocate exactly size(i8,i32))
- Items are near each other;
- Fast iteration and CPU apply some cycles reductions;
##### Pylist:
- Higher memory overhead(Python Objects are Heavy);
- Items are pointers to random locations with different distances;
- Items have python types and can;
- Slower iteration;
- CPU execution(native);
##### list(python side):
- Same as Pylist, unless on CPU execution(interpreted).
##### Pylist vs list:
- Pylist can be 2x–5x faster(iteration) thanks to the removal of interpreter overhead;
##### Vec vs Pylist:
- Vec can be 20-50x faster(iteration);
- Vec is stored at rust side and Pylist can be used as reference, avoiding memory allocation.
- Vec operations are at rust speed, Pylist operations at python speed.
1. std::collections::HashMap

This is a standard Rust hash map. When you use this in a PyO3 function, PyO3 automatically performs a conversion (extracting data from Python to Rust or serializing Rust data back to Python).
When to use it:

    Heavy Computation in Rust: You need to perform complex logic, filtering, or aggregations on the data. Rust's native HashMap is significantly faster for iteration and lookups than calling into the Python C-API.

    Releasing the GIL: You want to parallelize work using Rayon or standard threads. You must convert the data to a Rust HashMap first so you can release the GIL (py.allow_threads) and process it without blocking the Python interpreter.

    Type Safety: You require strict guarantees that keys are String and values are i32 (for example).

Performance Consideration (The "Conversion Tax"):

Using HashMap incurs an O(N) cost immediately upon function entry (to convert PyObject → Rust) and again on exit (Rust → PyObject).

    Good if: O(Computation)≫O(Conversion).

    Bad if: You only read one key and return.

### Good Practices FFI:
Prefer zero-copy approachs when possible