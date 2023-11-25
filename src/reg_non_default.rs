use regex_automata::meta::Regex;
use once_cell::sync::Lazy;
use std::time::Instant;

fn process(embalagem: &str, dsproduto: &str,
    re_brahm0: &Regex, re_brahm1: &Regex, re_brahm2: &Regex, re_brahm3: &Regex,
     re_brahm4: &Regex, re_brahm5: &Regex, re_brahm6: &Regex, re_brahm7: &Regex
     , re_brahm8: &Regex, re_brahm9: &Regex) -> Option<&'static str>{

    let start = Instant::now();
    if re_brahm0.is_match(dsproduto){
        if embalagem == "LATA 350 ML"{
            if re_brahm1.is_match(dsproduto) {
                return Some("BRAHMA DUPLO MALTE TOSTADA");
            }
            if re_brahm2.is_match(dsproduto){
                return Some("BRAHMA DUPLO MALTE ESCURA");
            }
            if re_brahm3.is_match(dsproduto){
                return Some("BRAHMA DUPLO MALTE TRIGO");
            }
        }
        if re_brahm4.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){
            return Some("BRAHMA MALZBIER");}
        if re_brahm5.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){return Some("BRAHMA EXTRA LAGER");}
            
        if re_brahm6.is_match(dsproduto){
            if re_brahm7.is_match(dsproduto) && ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem) {
                if re_brahm8.is_match(dsproduto){
                    return Some("BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)");
                }
                if re_brahm9.is_match(dsproduto){
                    return Some("BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)");
                    
                }
            }
            return Some("BRAHMA DUPLO MALTE");
        }
        if re_brahm7.is_match(dsproduto) && 
            ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem){
            if re_brahm8.is_match(dsproduto){
                return Some("BRAHMA CHOPP (PACK C/ 6 UNIDADES)");
            }
                
            if re_brahm9.is_match(dsproduto){
                return Some("BRAHMA CHOPP (PACK C/ 15 UNIDADES)");
            }
        }  
        return Some("BRAHMA CHOPP");
    }
    return None;
}
fn main() {

    let RE_BRAHM0 = Regex::new("BRAHM").unwrap();
    let RE_BRAHM1 = Regex::new("TOST").unwrap();
    let RE_BRAHM2 = Regex::new("ESCU").unwrap();
    let RE_BRAHM3 = Regex::new("TRIG").unwrap();
    let RE_BRAHM4 = Regex::new("MALZ").unwrap();
    let RE_BRAHM5 = Regex::new("XTR|LAGER").unwrap();
    let RE_BRAHM6 = Regex::new(r"DUPL|MALT|\bDM\b").unwrap();
    let RE_BRAHM7 = Regex::new("PAC?K?|C/?").unwrap();
    let RE_BRAHM8 = Regex::new(r"\b6\b").unwrap();
    let RE_BRAHM9 = Regex::new(r"\b15\b").unwrap();
    let embalagem = "LATA 310 ML";
    let dsproduto = r"BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT";
    let start = Instant::now();
    for _ in 0..100_000 {
        process(embalagem, dsproduto, &RE_BRAHM0, &RE_BRAHM1, &RE_BRAHM2, &RE_BRAHM3,
        &RE_BRAHM4, &RE_BRAHM5, &RE_BRAHM6, &RE_BRAHM7
        , &RE_BRAHM8, &RE_BRAHM9);
    }
    let elapsed = start.elapsed();
    println!("{:?}", elapsed); 
    let start = Instant::now();
    for _ in 0..100_000 {
        process(embalagem, dsproduto, &RE_BRAHM0, &RE_BRAHM1, &RE_BRAHM2, &RE_BRAHM3,
        &RE_BRAHM4, &RE_BRAHM5, &RE_BRAHM6, &RE_BRAHM7
        , &RE_BRAHM8, &RE_BRAHM9);
    }
    let elapsed = start.elapsed();
    println!("{:?}", elapsed); 
    let start = Instant::now();
    for _ in 0..100_000 {
        process(embalagem, dsproduto, &RE_BRAHM0, &RE_BRAHM1, &RE_BRAHM2, &RE_BRAHM3,
        &RE_BRAHM4, &RE_BRAHM5, &RE_BRAHM6, &RE_BRAHM7
        , &RE_BRAHM8, &RE_BRAHM9);
    }
    let elapsed = start.elapsed();
    println!("{:?}", elapsed); 
    let start = Instant::now();
    for _ in 0..100_000 {
        process(embalagem, dsproduto, &RE_BRAHM0, &RE_BRAHM1, &RE_BRAHM2, &RE_BRAHM3,
        &RE_BRAHM4, &RE_BRAHM5, &RE_BRAHM6, &RE_BRAHM7
        , &RE_BRAHM8, &RE_BRAHM9);
    }
    let elapsed = start.elapsed();
    println!("{:?}", elapsed); 
}
