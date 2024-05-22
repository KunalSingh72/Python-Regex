import numpy
def operations(a,b):
    c = []
    d = []
    for i in range(len(a)):
        c.append( a[i] + b [i] )
        d.append( a[i] - b [i]  )

    c.sort(reverse=True)
    d.sort(reverse=True)
    return max(c), min(c), max(d), min(d), c, d



'''
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum


def sorts(*args):
    return sorted(args,reverse=True)

'''