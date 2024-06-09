l=[]
n=int (input("Size:"))
print(n)
choice=int(input("Enter choice:\n1.Insert\n2.Delete\n3.Exit\n"))
print(choice)
for i in range(0,n):
    j=int(input())
    l.append(j)
print(l)
if(choice==1):
    s=int(input("Enter location:"))
    print(s)
    num=int(input("Enter element to insert:"))
    print(num)
    l.insert(s,num)
    print(num,"inserted at",s)
    print(l)
elif(choice==2):
    e=int(input("Enter location:"))
    print(e)
    print(l[e],"deleted from index",e)
    l.pop(e)
    print(l)
else:
    print("Exiting")
