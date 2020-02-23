# solution of second problem
lst_new = list(map(str,input().split(" 1")))
from itertools import permutations
p=list(permutations(lst_new))
max=0
for i in p:
    s=""
    for j in i:
        s=s+j
    if int(s)>max:
        max=int(s)
print(max)