l=[]
m=[]
n=int(input("Size:"))
print(n)
s=1
for i in range(0,n):
    j=int(input())
    l.append(j)
for k in range(0,n):
    p=int(input())
    m.append(p)
print("Elements of the first array:",l)
print("Elements of the second array:",m)
for x in range(0,n):
    if(l[x]==m[x]):
        s+=1
if(s>=n):
    print("Both arrays are equal")
else:
    print("Both arrays are not equal")


