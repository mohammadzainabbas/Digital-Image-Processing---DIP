#from collections import Iterable
import numpy as np
#By Recursion
def Flat(a):
    for parent in a:
        if not isinstance(parent, Iterable):
            yield parent
        else:
            for child in Flat(parent):
                yield child

#By iteration -- Much faster
def Flatten(a, ClassTypes=(list, tuple)):
    ClassType = type(a)
    if ClassType == int:
        return a
    else:
        a = list(a)
        i = 0
        while i < len(a):
            while isinstance(a[i], ClassTypes):
                if not a[i]:
                    a.pop(i)
                    i -= 1
                    break
                else:
                    a[i:i + 1] = a[i]
            i += 1
        a.sort()
        return ClassType(a)


###By iteration -- Much faster
##def Flatten(a, ClassTypes=(list, tuple)):
##    ClassType = type(a)
##    a = list(a)
##    i = 0
##    while i < len(a):
##        while isinstance(a[i], ClassTypes):
##            if not a[i]:
##                a.pop(i)
##                i -= 1
##                break
##            else:
##                a[i:i + 1] = a[i]
##        i += 1
##    return ClassType(a)

##def Flatten(a):
##    i = 0
##    while i < len(a):
##        while isinstance(a[i],list):
##            if not a[i]:
##                a.pop(i)
##                i -= 1
##                break
##            else:
##                a[i:i + 1] = a[i]
##        i += 1
##    return a

a = [1,2,[3,4,5,[43,932,808,[87,872],[1,2,3,4,[5,4,32,45,21]]],977,897],797,[51,2,3,4]]
##a = []
##for i in range(3):
##  a = [a, i]
b=[]
d=[]
for i in range(len(a)):
    b.append(Flatten(a[i]))
    if type(a[i])==list:
        d.append(np.unique(Flatten(a[i])).tolist())
    else:
        d.append(a[i])
    #d=Flatten(d)
    a.pop(i)
    a.insert(i,b[i])
print(b)
#print(a)
print(d)
#c = list(sorted(b))
#b = list(Flat(a))
#print(c)
#c.remove(4)
