s1=input()
s2=input()
l1=len(s1)
l2=len(s2)
ls1=list(s1)
ls2=list(s2)
sls1=sorted(ls1)
sls2=sorted(ls2)
for i in range(0,l1):
    if sls1[i]!=sls2[i]:
        print(sls2[i])

