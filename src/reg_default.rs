use {
    once_cell::sync::Lazy,
    regex::Regex,
};
use std::time::Instant;

fn process(embalagem: &str, dsproduto: &str) -> Option<&'static str>{
    static RE_BRAHM0: Lazy<Regex> = Lazy::new(|| Regex::new("BRAHM").unwrap());
    static RE_BRAHM1: Lazy<Regex> = Lazy::new(|| Regex::new("TOST").unwrap());
    static RE_BRAHM2: Lazy<Regex> = Lazy::new(|| Regex::new("ESCU").unwrap());
    static RE_BRAHM3: Lazy<Regex> = Lazy::new(|| Regex::new("TRIG").unwrap());
    static RE_BRAHM4: Lazy<Regex> = Lazy::new(|| Regex::new("MALZ").unwrap());
    static RE_BRAHM5: Lazy<Regex> = Lazy::new(|| Regex::new("XTR|LAGER").unwrap());
    static RE_BRAHM6: Lazy<Regex> = Lazy::new(|| Regex::new(r"DUPL|MALT|\bDM\b").unwrap());
    static RE_BRAHM7: Lazy<Regex> = Lazy::new(|| Regex::new("PAC?K?|C/?").unwrap());
    static RE_BRAHM8: Lazy<Regex> = Lazy::new(|| Regex::new(r"\b6\b").unwrap());
    static RE_BRAHM9: Lazy<Regex> = Lazy::new(|| Regex::new(r"\b15\b").unwrap());
    if RE_BRAHM0.is_match(dsproduto){
        if embalagem == "LATA 350 ML"{
            if RE_BRAHM1.is_match(dsproduto) {
                return Some("BRAHMA DUPLO MALTE TOSTADA");
            }
            if RE_BRAHM2.is_match(dsproduto){
                return Some("BRAHMA DUPLO MALTE ESCURA");
            }
            if RE_BRAHM3.is_match(dsproduto){
                return Some("BRAHMA DUPLO MALTE TRIGO");
            }
        }
        if RE_BRAHM4.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){
            return Some("BRAHMA MALZBIER");}
        if RE_BRAHM5.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){return Some("BRAHMA EXTRA LAGER");}
            
        if RE_BRAHM6.is_match(dsproduto){
            if RE_BRAHM7.is_match(dsproduto) && ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem) {
                if RE_BRAHM8.is_match(dsproduto){
                    return Some("BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)");
                }
                if RE_BRAHM9.is_match(dsproduto){
                    return Some("BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)");
                    
                }
            }
            return Some("BRAHMA DUPLO MALTE");
        }
        if RE_BRAHM7.is_match(dsproduto) && 
            ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem){
            if RE_BRAHM8.is_match(dsproduto){
                return Some("BRAHMA CHOPP (PACK C/ 6 UNIDADES)");
            }
                
            if RE_BRAHM9.is_match(dsproduto){
                return Some("BRAHMA CHOPP (PACK C/ 15 UNIDADES)");
            }
        }  
        return Some("BRAHMA CHOPP");
    }
    return None;
}
fn main() {
    let embalagem = "LATA 310 ML";
    let dsproduto = r"BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT";
    let mut a = None;
    a = process(embalagem, dsproduto);
    let start = Instant::now();
    for _ in 0..100_000 {
        process(embalagem, dsproduto);
    }
    let elapsed = start.elapsed();
    println!("{:?}", elapsed); 
    println!("{:?}", a);
}
