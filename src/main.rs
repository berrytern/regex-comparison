use {
    once_cell::sync::Lazy,
    regex::Regex,
};
use std::time::Instant;

fn regex_replace(dsproduto: &str) -> String {
    static RE_BRAHM0: Lazy<Regex> = Lazy::new(|| Regex::new("FD").unwrap());
    RE_BRAHM0.replace(dsproduto, "1 KG").to_string()
}
fn string_replace(dsproduto: &str) -> String {
    dsproduto.replace("FD", "1 KG")
}
fn main() {
    let dsproduto = r"arroz com farofa FD 1 real";
    let a = regex_replace(dsproduto);
    let start = Instant::now();
    for _ in 0..100_000 {
        regex_replace(dsproduto);
    }
    let elapsed = start.elapsed();
    println!("regex replace: {:?}", elapsed); 
    let start = Instant::now();
    for _ in 0..100_000 {
        string_replace(dsproduto);
    }
    let elapsed = start.elapsed();
    println!("string replace: {:?}", elapsed); 
    println!("{:?}", a);
}
