
echo "-----------\tBenchmark Script\t-----------"
source ./.venv/bin/activate
cargo build --release
# uv sync
maturin develop --release
echo "-----------\tStart of Benchmark\t-----------"
uv run python re_non_compiled.py 
uv run python re_compiled.py
uv run python re_rust.py
uv run python calling_rust.py

echo "-----------\tString replace Benchmark\t-----------"
echo "Python side:"
uv run python re_sub.py
echo "Rust side:"
cargo run --release
echo "-----------\tEnd of Benchmark\t-----------"