'''
Armstrong Number : 

num = int(input("Enter number : "))
original_value = num
power = 0
while(num>0):
    power +=1
    num=num//10
sum=0
num = original_value
while(num>0):
    rem=num%10
    sum = sum + rem**power
    num//=10

if sum == original_value:
    print("Armstrong")
else:
    print("Not Armstrong")

    '''

 #   Q  -- 1+2+3+4+5+6+7+2+3+4+5+6+7+8+3+4+5+6+7+8+9



# dict = {1 : 'red', 2 : 'ter', 3 : 'wer'}
dict1 = {}
# for i in "hello":
#     dict1[i] = 1
# print(dict1)

# for i in "Hey tushar hello":
#     if i in dict1:
#         dict1[i] +=1
#     elif i in "aeiouAEIOU":
#         dict1[i] = 1
# print(dict1) 


