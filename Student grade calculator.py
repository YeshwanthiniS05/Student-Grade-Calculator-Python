n=int(input("Enter No. of Subjects:"))
sum=0
m=[]
for i in range(1,n+1):
    a=int(input("Enter mark of subject"+str(i)+":"))
    m.append(a)
    sum+=a
avg=sum/n
print("Total marks of",n,"subjects is",sum)
print("Average mark is",avg)
if avg>=90:
    print("Your Grade is A")
elif avg>=75:
    print("Your Grade is B")
elif avg>=60:
    print("Your Grade is C")
elif avg>=50:
    print("Your Grade is D")
else:
    print("Your Grade is F")
fail=False
for mark in m:
    if mark<50:
        fail=True
        break
if fail:
    print("Fail")
else:
    print("Pass")            