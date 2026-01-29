from regex_comparison import process
from timeit import timeit


time = timeit("process('LATA 310 ML', 'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT')", number=100000, setup="""
import re
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
from regex_comparison import process
process('LATA 310 ML', 'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT')
              """)
import re


print("-----------\tCalling rust (bulk)\t-----------")
print(f'{time*1000}ms')
# print(process('LATA 310 ML', 'BRAHMA DUPLO MALTE LT 310ML SH C/15 MULT'))
