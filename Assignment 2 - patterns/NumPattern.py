'''
1
12
123
1234

'''
for i in range(1,5):
    for j in range(1,i+1):
        print(j,  end=" ")
    print()


print()
'''
1
23
456
78910
'''

a=1
for i in range(1,5):
    for j in range(1,i+1):
        print(a,  end=" ")
        a+=1
    print()


print()
'''
10
98
765
4321
'''

a=10
for i in range(1,5):
    for j in range(1,i+1):
        print(a,  end=" ")
        a-=1
    print()