l=[]
n=int(input("Size:"))
print(n)
temp=0
for i in range(0,n):
    j=int(input())
    l.append(j)
print(l)
for k in range(0,n):
    for m in range(k+1,n):
        if(l[k]>l[m]):
            temp=l[m]
            l[m]=l[k]
            l[k]=temp
print("Smallest number:",l[0])
print("Largest number:",l[n-1])
