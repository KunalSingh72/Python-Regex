'''   
   A
  BC
 DEF
GHIJ    
'''
a=65
for i in range(1,5):
    for j in range(4-i):
        print(end=" ") 
    for k in range(0,i):
        print(chr(a),end="")
        a+=1
    print()