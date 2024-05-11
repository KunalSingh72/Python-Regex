'''
*
**
***
****
'''


for i in range(1,6):
    for j in range(0,i):
        if j==0 or j==i-1 or i==5:
            print("*",end="")
        else:
            print(" ",end="")
    print()