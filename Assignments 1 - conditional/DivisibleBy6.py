'''
Q3 Take two number from the user and check whether both the number are divisble
by 6
( divisibility rule say it should be divided by 2 and 3)
'''

x=int(input("Enter number 1 : "))
y=int(input("Enter number 1 : "))

if x%6==0 and y%6==0:
    print("Both numbers are divisible by 6")
else:
    print("Both numbers are not divisible by 6")