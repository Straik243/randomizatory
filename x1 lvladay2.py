import copy
from itertools import groupby
x = ['h', 'e', 'l', 'l', 'o','a','d','d','o','n','n','i','s']
x1 = list(set(x))
new_list = copy.deepcopy(x1)
new_list.remove(new_list[0])
new_list.remove(new_list[2])
new_list.remove(new_list[3])
print(new_list)