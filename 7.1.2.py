s=input()
l=len(s)
x=input()
y=input()
for i in range(0,l):
        if(s[i]==x):
          s1=s.replace(s[i],y)
          break
print(s1)
    

