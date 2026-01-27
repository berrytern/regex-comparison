# Regex Performance Comparison: Rust vs Python

This repository benchmarks Regular Expression (Regex) performance between **Rust** and **Python**, specifically focusing on the impact of **compilation strategies** and **initialization overhead**.

The goal is to demonstrate how proper static initialization (using `once_cell::sync::Lazy` in Rust) allows the regex engine to outperform Python significantly, whereas improper runtime compilation can lead to poor performance.

## ⚡ Benchmark Results

Results based on **100,000 iterations** of a complex pattern matching task.

### 🔍 Search / Match Performance

| Strategy | Time | Notes |
| :--- | :--- | :--- |
| **Rust (Lazy Static)** | **~33 ms** | Compiled once, reused (Zero-overhead) |
| **Python (Calling Rust)** | ~66 ms | FFI overhead included |
| **Python (Compiled)** | ~276 ms | Using `re.compile()` beforehand |
| **Python (Non-Compiled)** | ~867 ms | Compiling inline every iteration |

### 🔄 Replace / Sub Performance

| Strategy | Time | Notes |
| :--- | :--- | :--- |
| **Rust (String Replace)** | **~11 ms** | Native string replacement |
| **Rust (Regex Replace)** | ~17 ms | `Regex::replace` |
| **Python (String Replace)** | ~20 ms | Native `.replace()` |
| **Python (Compiled Regex)** | ~47 ms | `re_compiled.sub()` |
| **Python (Non-Compiled)** | ~127 ms | `re.sub()` inline |

---

## 🧠 Key Takeaways

### 1. The Cost of Compilation
In Rust, `Regex::new(...)` is an expensive operation because it compiles the pattern into a **Deterministic Finite Automaton (DFA)** to guarantee linear-time search.
- **Bad Practice:** initializing `Regex::new` inside a loop. This forces re-compilation every time, killing performance.
- **Best Practice:** Using `once_cell::sync::Lazy` (or `std::sync::OnceLock`) to initialize the regex **once** on the first use and reuse it globally.

### 2. Python vs. Rust Optimizations
- **Python** uses a backtracking engine. It starts fast but can be slower on complex matches. It creates a cache for recently used patterns, which mitigates some "non-compiled" penalties but still incurs lookup overhead.
- **Rust** uses a DFA engine (via the `regex` and `regex-automata` crates). Once compiled, the matching phase is extremely fast and predictable, as shown in the **33ms** result vs Python's **276ms**.

## 🛠️ Technologies Used

- **Rust**: `1.76.0-nightly`
  - Crates: `regex`, `once_cell`, `regex-automata`
- **Python**: `3.8.16`

## 📦 Installation & Setup

This project uses **Maturin** to build and install the Rust extension for Python.

### 1. Prerequisites
- **Rust**: [Install via rustup](https://rustup.rs/)
- **Python 3.8+**
- **uv**: [Install via standalone installer](https://docs.astral.sh/uv/getting-started/installation/)
- **Maturin**: install via uv: 
  ```bash
  uv tool install maturin
  ```

### 2. Compile & Install
To get the valid performance numbers, you must compile in release mode. Debug builds in Rust are significantly slower (up to 100x for regex) and will skew your results.

#### Option A:
Development Build (Recommended) Installs the package directly into your current Python environment.
```bash
maturin develop --release
```
#### Option B: Build Wheel
Builds a .whl file in target/wheels which you can install manually.
```bash
maturin build --release
uv pip install target/wheels/regex_comparison-*.whl
```

## 🚀 How to Run

### Rust Benchmarks
To get accurate numbers, always run with the release flag:
```bash
cargo run --release
```
### Python Benchmarks
Run the individual scripts to test different scenarios:
```bash
uv run python calling_rust.py
uv run python re_compiled.py
uv run python re_non_compiled.py
uv run python re_sub.py
```