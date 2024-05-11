'''

Q2:
take 3 number as input from a user as 3 side of a triangle
and check whether it will create a triagle or not
'''

a = int(input("Enter 1 side : "))
b = int(input("Enter 2 side : "))
c = int(input("Enter 3 side : "))

if(((a+b)>c) and  ((b+c)>a) and  ((a+c)>b)):
    print("Given sides are of a triangle")
else:
    print("Given sides are not of a triangle")

