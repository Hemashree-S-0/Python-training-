l=[]
ml=[]
n=int(input("Size:"))
print(n)
temp=0
tp=0
for i in range(0,n):
    j=int(input())
    l.append(j)
print(l)
for i in range(0,n):
    x=int(input())
    ml.append(x)
print(ml)
for k in range(0,n):
    for m in range(k+1,n):
        if(l[k]<l[m]):
            temp=l[m]
            l[m]=l[k]
            l[k]=temp
maxi=l[0]
for k in range(0,n):
    for m in range(0,n):
        if(ml[k]<ml[m]):
            tp=ml[m]
            ml[m]=ml[k]
            ml[k]=tp
mini=ml[0]
print("Maximum of first array:",maxi)
print("Minimum of second array:",mini)
print("product:",maxi*mini)

