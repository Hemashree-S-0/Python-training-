import math as mt
l=[]
s=0
t=0
n=int(input())
for i in range(0,n):
    j=float(input())
    l.append(j)
    s=s+j
print(l)
mean=s/n
for k in range(0,n):
    t=t+mt.pow((l[i]-mean),2)
var=t/n
dev=mt.sqrt(var)
print(f"Mean:{mean:.2f}")
print(f"Variance:{var:.2f}")
print(f"Deviation:{dev:.2f}")
    






