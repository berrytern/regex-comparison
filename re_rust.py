import reru as re
from timeit import timeit

times = 100000 # 100000

time = timeit("process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
def process(dsproduto, embalagem):
    if re.search(r"BRAHM", dsproduto):
        if embalagem == "LATA 350 ML":
            if re.search(r"TOST", dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if re.search(r"ESCU", dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if re.search(r"TRIG", dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if re.search(r"MALZ", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if re.search(r"XTR|LAGER", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if re.search(r"DUPL|MALT|\bDM\b", dsproduto):
            if re.search(r"PAC?K?|C/?", dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if re.search(r"\b6\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if re.search(r"\b15\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if re.search(r"PAC?K?|C/?", dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if re.search(r"\b6\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if re.search(r"\b15\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')""")


compiled_reru_time = timeit("process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process(dsproduto, embalagem):
    if RE_BRAHM0.search(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.search(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.search(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.search(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.search(dsproduto):
            if RE_BRAHM7.search(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.search(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")

compiled_flpc_time = timeit("process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import flpc as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process(dsproduto, embalagem):
    if re.search(RE_BRAHM0, dsproduto):
        if embalagem == "LATA 350 ML":
            if re.search(RE_BRAHM1, dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if re.search(RE_BRAHM2, dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if re.search(RE_BRAHM3, dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if re.search(RE_BRAHM4, dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if re.search(RE_BRAHM5, dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if re.search(RE_BRAHM6, dsproduto):
            if re.search(RE_BRAHM7, dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if re.search(RE_BRAHM8, dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if re.search(RE_BRAHM9, dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if re.search(RE_BRAHM7, dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if re.search(RE_BRAHM8, dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if re.search(RE_BRAHM9, dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")


rure_time = timeit("process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import rure as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process(dsproduto, embalagem):
    if RE_BRAHM0.search(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.search(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.search(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.search(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.search(dsproduto):
            if RE_BRAHM7.search(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.search(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')""")


def process(dsproduto, embalagem):
    if re.search(r"BRAHM", dsproduto):
        if embalagem == "LATA 350 ML":
            if re.search(r"TOST", dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if re.search(r"ESCU", dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if re.search(r"TRIG", dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if re.search(r"MALZ", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if re.search(r"XTR|LAGER", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if re.search(r"DUPL|MALT|\bDM\b", dsproduto):
            if re.search(r"PAC?K?|C/?", dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if re.search(r"\b6\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if re.search(r"\b15\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if re.search(r"PAC?K?|C/?", dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if re.search(r"\b6\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if re.search(r"\b15\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'

time_is_search = timeit("process_is_search('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')", number=times, setup="""
import reru as re
def process_is_search(dsproduto, embalagem):
    if re.is_search(r"BRAHM", dsproduto):
        if embalagem == "LATA 350 ML":
            if re.is_search(r"TOST", dsproduto):   
                return "BRAHMA DUPLO MALTE TOSTADA"
            if re.is_search(r"ESCU", dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if re.is_search(r"TRIG", dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if re.is_search(r"MALZ", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if re.is_search(r"XTR|LAGER", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if re.is_search(r"DUPL|MALT|\bDM\b", dsproduto):
            if re.is_search(r"PAC?K?|C/?", dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if re.is_search(r"\b6\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if re.is_search(r"\b15\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if re.is_search(r"PAC?K?|C/?", dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if re.is_search(r"\b6\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if re.is_search(r"\b15\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'        
process_is_search('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')
""")

rure_time_is_match = timeit("process_is_match(u'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', u'LATA 310 ML')", number=times, setup="""
import rure as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process_is_match(dsproduto, embalagem):
    if RE_BRAHM0.is_match(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.is_match(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.is_match(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.is_match(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.is_match(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.is_match(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.is_match(dsproduto):
            if RE_BRAHM7.is_match(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.is_match(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.is_match(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.is_match(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.is_match(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.is_match(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process_is_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")

compiled_reru_time_is_search = timeit("process_is_search(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process_is_search(dsproduto, embalagem):
    if RE_BRAHM0.is_search(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.is_search(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.is_search(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.is_search(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.is_search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.is_search(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.is_search(dsproduto):
            if RE_BRAHM7.is_search(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.is_search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.is_search(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.is_search(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.is_search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.is_search(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process_is_search(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")

time_match = timeit("process_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
def process_match(dsproduto, embalagem):
    if re.match(r"BRAHM", dsproduto):
        if embalagem == "LATA 350 ML":
            if re.match(r"TOST", dsproduto):   
                return "BRAHMA DUPLO MALTE TOSTADA"
            if re.match(r"ESCU", dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if re.match(r"TRIG", dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if re.match(r"MALZ", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if re.match(r"XTR|LAGER", dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if re.match(r"DUPL|MALT|\bDM\b", dsproduto):
            if re.match(r"PAC?K?|C/?", dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if re.match(r"\b6\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if re.match(r"\b15\b", dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if re.match(r"PAC?K?|C/?", dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if re.match(r"\b6\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if re.match(r"\b15\b", dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'        
process_match('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')
""")

compiled_reru_time_match = timeit("process_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process_match(dsproduto, embalagem):
    if RE_BRAHM0.match(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.match(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.match(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.match(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.match(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.match(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.match(dsproduto):
            if RE_BRAHM7.match(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.match(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.match(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.match(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.match(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.match(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")

alt_compiled_reru_time_match = timeit("process_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')", number=times, setup="""
import reru as re
RE_BRAHM0 = re.compile(r"BRAHM")
RE_BRAHM1 = re.compile(r"TOST")
RE_BRAHM2 = re.compile(r"ESCU")
RE_BRAHM3 = re.compile(r"TRIG")
RE_BRAHM4 = re.compile(r"MALZ")
RE_BRAHM5 = re.compile(r"XTR|LAGER")
RE_BRAHM6 = re.compile(r"DUPL|MALT|\bDM\b")
RE_BRAHM7 = re.compile(r"PAC?K?|C/?")
RE_BRAHM8 = re.compile(r"\b6\b")
RE_BRAHM9 = re.compile(r"\b15\b")
def process_match(dsproduto, embalagem):
    if RE_BRAHM0.find_indices(dsproduto):
        if embalagem == "LATA 350 ML":
            if RE_BRAHM1.find_indices(dsproduto):
                return "BRAHMA DUPLO MALTE TOSTADA"
            if RE_BRAHM2.find_indices(dsproduto):
                return "BRAHMA DUPLO MALTE ESCURA"
            if RE_BRAHM3.find_indices(dsproduto):
                return "BRAHMA DUPLO MALTE TRIGO"
        if RE_BRAHM4.find_indices(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA MALZBIER"
        if RE_BRAHM5.find_indices(dsproduto) and embalagem in [
            "LATA 350 ML",
            "GARRAFA LONG NECK LN ONE WAY DESCARTAVEL 355 ML",
        ]:
            return "BRAHMA EXTRA LAGER"
        if RE_BRAHM6.find_indices(dsproduto):
            if RE_BRAHM7.find_indices(dsproduto) and embalagem in [
                "LATA 310 ML",
                "LATA 410 ML",
            ]:
                if RE_BRAHM8.find_indices(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/ 6 UNIDADES)"
                if RE_BRAHM9.find_indices(dsproduto):
                    return "BRAHMA DUPLO MALTE (PACK C/15 UNIDADES)"
            return "BRAHMA DUPLO MALTE"
        if RE_BRAHM7.find_indices(dsproduto) and embalagem in [
            "LATA 310 ML",
            "LATA 410 ML",
        ]:
            if RE_BRAHM8.find_indices(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 6 UNIDADES)"
            if RE_BRAHM9.find_indices(dsproduto):
                return "BRAHMA CHOPP (PACK C/ 15 UNIDADES)"
        return 'BRAHMA CHOPP'
process_match(r'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', r'LATA 310 ML')
""")

print("-----------\treru compiled\t-----------")
print("reru search time:")
print(f'{time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("reru compiled search time:")
print(f'{compiled_reru_time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("flpc compiled search time:")
print(f'{compiled_flpc_time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))

print("reru is_search time:")
print(f'{time_is_search*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("reru compiled is_search time:")
print(f'{compiled_reru_time_is_search*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("reru match time:")
print(f'{time_match*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("reru compiled match time:")
print(f'{compiled_reru_time_match*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("reru alt compiled match time:")
print(f'{alt_compiled_reru_time_match*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("-----------\trure compiled\t-----------")


print("rure search time:")
print(f'{rure_time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
print("rure is_match time:")
print(f'{rure_time_is_match*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))

