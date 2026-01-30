from timeit import timeit


time = timeit("process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')", number=100000, setup="""
import re
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


match_time = timeit("process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')", number=100000, setup="""
import re
def process(dsproduto, embalagem):
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
process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML')""")

import re


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

print("-----------\tDefault re non-compiled\t-----------")
print("search time:")
print(f'{time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))

print("match time:")
print(f'{match_time*1000}ms')
# print(process('BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT', 'LATA 310 ML'))
