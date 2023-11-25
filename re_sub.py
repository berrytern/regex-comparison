from timeit import timeit


import re
re_0 = re.compile("FD")
a = re_0.sub("1 KG", "arroz com farofa FD 1 real")
time_compiled = timeit('re_0.sub("1 KG", description)', number=100000, setup="""
import re
re_0 = re.compile("FD")
description = "arroz com farofa FD 1 real"
""")
time = timeit('re.sub("FD", "1 KG", description)', number=100000, setup="""
import re
description = "arroz com farofa FD 1 real"
""")

print(f'non-compiled: {time*1000:.3f}ms')
print(f'compiled: {time_compiled*1000:.3f}ms')
print(f"output: {a}")
