
echo "-----------\tBenchmark Script\t-----------"
source ./.venv/bin/activate
cargo build --release
# uv sync
maturin develop --release
echo "-----------\tStart of Benchmark\t-----------"
python re_non_compiled.py 
python re_compiled.py
python re_rust.py
python calling_rust.py

echo "-----------\tString replace Benchmark\t-----------"
echo "Python side:"
python re_sub.py
echo "Rust side:"
cargo run --release
echo "-----------\tEnd of Benchmark\t-----------"