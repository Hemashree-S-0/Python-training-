l=[]
h=[]
n=int(input())
for i in range(0,n):
    j=int(input())
    l.append(j)
print(l)
for k in range(0,n):
    for m in range(k+1,n):
        if(l[k]==l[m]):
            l[m]='a'
print("Unique elements in the array:",end=" ")
for p in range(0,n):
    if(l[p]!='a'):
        h.append(l[p])
print(h)
    







