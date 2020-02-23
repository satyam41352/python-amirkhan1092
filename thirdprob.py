#solution to problem third
n = int(input())
b = bin(n)[2:]
one_l = [i for i in b.split("0") if i != '']
one_l.sort(key=len)
print(len(one_l[-1]))