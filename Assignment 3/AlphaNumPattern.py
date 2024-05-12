'''
ABCD1
ABC12
AB123
A1234
'''

for i in range(1,5):
    a=65
    n=1
    for j in range(5-i):
        print(chr(a),end="")
        a+=1
    for k in range(0,i):
        print(n,end="")
        n+=1
    print()

''' 
ABCD1
EFG23
HI456
J78910

'''
n=1
for i in range(1,5):
    a=65

    for j in range(5-i):
        print(chr(a),end="")
        a+=1
    for k in range(0,i):
        print(n,end="")
        n+=1
    print()