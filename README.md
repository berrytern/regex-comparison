## Language versions
- Python 3.8.16
- Rust 1.76.0-nightly

## Speed Comparison over 100_000 iterations
### is_match / search
- Rust
    ```sh
    33.001282ms
    Some("BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)")
    ```
- Python  compiled
    ```sh
    276.98562500154367ms
    BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)
    ```
- Python non-compiled
    ```sh
    867.1785770020506ms
    BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)
    ```
### replace / sub
- Rust
    ```sh
    regex replace: 17.787219ms
    string replace: 11.158391ms
    ```
- Python
    ```sh
    non-compiled: 127.899ms
    compiled: 47.473ms
    ```