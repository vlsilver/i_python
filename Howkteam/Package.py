import vl_package.module_1, vl_package.module_2 as m
vl_package.module_1.f_1()
print(vl_package.module_1.var_1)
vl_package.module_2.f_2()
print(vl_package.module_2.var_2)
m.f_2()
print(m.var_2)

from vl_package import module_1 as m_1, module_2 as m_2
print(m_1.var_1)
print(m_2.var_2)

import vl_package #import san trong file __init__
vl_package.m1.f_1()
vl_package.m2.f_2()

from vl_package import* #phai quy dinh __all__ la gi trong file __init__
m1.f_1()
m2.f_2()