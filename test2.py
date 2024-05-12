password = input("Enter Your Password : ")
capital = 0 
small = 0
num = 0
special_char = 0
for i in password:
    for c in range(65,91):
        if i==chr(c):
            capital+=1
    for s in range(97,123):
        if i==chr(s):
            small+=1
    if i in "0123456789":
        num+=1
    if i in "#@!":
        special_char +=1

if capital>=3 and small>=2 and num>=1 and special_char>=1 and 15>len(password)>=5:
    print("Valid Password")
else:
    print("Invalid Password")