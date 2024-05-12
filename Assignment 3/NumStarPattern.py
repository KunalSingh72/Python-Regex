'''
1234*
567**
89***
'''

a = 1
for i in range(1,4):
    for j in range(5-i):
        print(a,end="")
        a+=1
    for k in range(0,i):
        print("*",end="")
    print()


    