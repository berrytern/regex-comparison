use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;
use {
    once_cell::sync::Lazy,
    regex::Regex, // no backtrack
    // fancy_regex::Regex as Regex2, // backtrack
};

#[pyfunction]
fn process(embalagem: &str, dsproduto: &str) -> PyResult<Option<&'static str>>{
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
                return Ok(Some("BRAHMA DUPLO MALTE TOSTADA"));
            }
            if RE_BRAHM2.is_match(dsproduto){
                return Ok(Some("BRAHMA DUPLO MALTE ESCURA"));
            }
            if RE_BRAHM3.is_match(dsproduto){
                return Ok(Some("BRAHMA DUPLO MALTE TRIGO"));
            }
        }
        if RE_BRAHM4.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){
            return Ok(Some("BRAHMA MALZBIER"));
        }
        if RE_BRAHM5.is_match(dsproduto) && [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ].contains(&embalagem){return Ok(Some("BRAHMA EXTRA LAGER"));}
            
        if RE_BRAHM6.is_match(dsproduto){
            if RE_BRAHM7.is_match(dsproduto) && ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem) {
                if RE_BRAHM8.is_match(dsproduto){
                    return Ok(Some("BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"));
                }
                if RE_BRAHM9.is_match(dsproduto){
                    return Ok(Some("BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"));
                }
            }
            return Ok(Some("BRAHMA DUPLO MALTE"));
        }
        if RE_BRAHM7.is_match(dsproduto) && 
            ["LATA 310 ML",
            "LATA 410 ML"].contains(&embalagem){
            if RE_BRAHM8.is_match(dsproduto){
                return Ok(Some("BRAHMA CHOPP (PACK C/ 6 UNIDADES)"));
            }
                
            if RE_BRAHM9.is_match(dsproduto){
                return Ok(Some("BRAHMA CHOPP (PACK C/ 15 UNIDADES)"));
            }
        }  
        return Ok(Some("BRAHMA CHOPP"));
    }
    return Ok(None);
}


/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn regex_comparison(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(process))?;
    Ok(())
}