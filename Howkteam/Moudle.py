#import <name moudle(name of python fiel).......> ( when use must have use name moudle)
#from <moudle> import <function, variable> (import function, variable....)
#from <moudle> import* ( import all object in moudle)
#<moudle>.<function>
#<moudle>.<variable-global>
import moudlevla # chinh sua truc tiep cac bien
moudlevla.say("Đây là bài học về Moudle")
moudlevla.say("Đang gọi hàm từ một file khác - file này được gọi là Moudle")
moudlevla.f_moudle()
print(type(moudlevla))
print(moudlevla.var_moudle)

from moudlevla import f_moudle,var_moudle
f_moudle()
print(var_moudle)

from moudlevla import*
print(var_moudle)
f_moudle()

from moudlevla import var_f2, lst_f2 #copy cai gia tri tu moudle(tru cac object tham chieu nhu list)
print(var_f2)
print(lst_f2)
var_f2 = 0
lst_f2[0] = 100
from moudlevla import var_f2, lst_f2
print(var_f2) # Gia tri nay khong doi
print(lst_f2) # Gia tri nay bi doi, vi do la list

from importlib import reload
reload(moudlevla)
print(lst_f2) #khong reload lai duoc list

import moudlevla as vl #doi ten moudle
from moudlevla import f_moudle as f
print(vl.var_f2)
print(f())

