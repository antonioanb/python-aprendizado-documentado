#count é um iteravel sem fim, diferente do range ele tambem é um irerator

from itertools import count

c1 = count(8, 8)
c2 = range(10)
#comparação com range
print("count tem __iter__ =", hasattr(c1, "__iter__"))
print("count tem __next__ =", hasattr(c1, "__next__"))
print("--" *30)
print("range tem __iter__ =", hasattr(c2, "__iter__"))
print("range tem __next__ =", hasattr(c2, "__next__"))

#count(start, step, ) ou nomeados  count(step= 8, start= 8)

#percorrendo
for i in c1:
    if i >=100:
        break
    print(i)