import random
r=random.randint(1,4)
a=r

if(a==1):
    a='stone'
elif(a==2):
    a='paper'
else:
    a='sizer'

i=input("Enter Your Choice Here:")
print("Your Choice is:"+i)
print("Computer Choice:"+a)

if(a=='stone' and i=='stone'):
    print("Tie")
elif(a=='stone' and i=='paper'):
    print("You Won !")
elif(a=='stone' and i=='sizer'):
    print("Computer Won !")
elif(a=='paper' and i=='stone'):
    print("Computer Won!")
elif(a=='paper' and i=='paper'):
    print("Tie")
elif(a=='paper' and i=='sizer'):
    print("You Won !")
elif(a=='sizer' and i=='stone'):
    print("You Won!")
elif(a=='sizer' and i=='paper'):
    print("Computer Won !")
elif(a=='sizer' and i=='sizer'):
    print("Tie")
else:
    print("Please Enter a Valid Input here :)............")
