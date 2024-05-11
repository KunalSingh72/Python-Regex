'''
Q1 user input on number of unit in integer
- for the starting 10 unit price is 50 rs each
- for the next 20 unit price is 20 rs each
- for the rest of unit price will be 10rs
calculate the total price
100  =>  500  +400 +700
90
70


'''

x=int(input("Enter' number : "))

if x<=10:
    print("Price : ", x*50)
elif x>10 and x<=30:
    print("Price : ", (500+((x-10)*20)))
else:
    print("Price : ", (500+400+(x-30)*10))

