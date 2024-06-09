l=[]
s=0
n=int(input())
for i in range(0,n):
    j=int(input())
    l.append(j)
print(l)
for k in range(0,n):
    for m in range(k+1,n):
        if(l[k]==l[m]):
            a=l[m]
            s+=1
if(s>0):
    print("Repeated elements in the array:",a)
else:
    print("Array elements not repeated")
