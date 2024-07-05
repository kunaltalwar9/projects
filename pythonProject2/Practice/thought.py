'''
str= input()
var=[]
def repeat():
    for i in range(0,len(str)):
        var.append(i)
        for j in var:
            if var[j] == str[i]:
                return j

import

elemsnt= findelementbyid=['']
switchtowindow.click(elemnst)
var= findelementbyvalue=''
assert var.isvissible(), switchtowindowbyindex[2]

elemt2= findelementbyid[''
switchtowindow.click
improt maths
a=2
b=3
class ABC:
    add a+b
    var= 55

    class CDED extends ABC:
        add b+c
        e= var+ b

for i in range(1,11):
    if i%2!=0:
        print(i)



ip = [7,2,5,9,3,8]
op = []
k = len(ip)
print(k)
#o/p: 7,9,8  while j == 3:
j = 0

for i in range(0, k+1):
    if ip[i] > ip[i+1]:
        pass
    else:
        print("ABCD")

print(ip)
'''
'''

ip = [7,2,5,9,3,8]
op = []
k = len(ip)
print(k)
#o/p: 7,9,8  while j == 3:
j = 0


for i in range(0, k-1):
    for j in range(i):
    #while ip[i] < ip[i+1]:
        if ip[i] > ip[i+1]:
            pass
        else:
            op = ip[i + 1]
            ip[i + 1] = ip[i]
            ip[i] = op
            op = []
#        ip[i] = max(ip[i],ip[i+1])

print(ip)
'''
'''
list1 = [56, 3, 2, 0, 7, 20]
# l = len(list1)


def swap(list1):
    if len(list1) == 1:
        return list1
    else:
        for i in range(0, len(list1)-1):
            for j in range(i):
                list1[j] = min(list1[j])
            return swap(list1[i+1:]) # +list1[0]
        print(swap(list1))

'''
'''


rs = int(input("Enter amount"))
coins = [1,2,5,10]
count = 0
class meth:
    def total(self,rs):
        for i in range(1,10):
            rs = rs - (10 * i)

            while rs > 0:
                count = rs
                return meth.total(rs)
        
                  
obj = meth()
obj.total(rs)
'''

'''
rs = int(input("Enter amount"))
coins = [1,2,5,10]
count = 0

abc = []
klm = []
def total(rs):
    for i in range(1, 10):
        rs = rs - (10 * i)
        j = 0
        while rs > 0:
           # j = j + 1
           # print(j)
           # klm.append(j)
            abc.append(rs)
            return total(rs)#, j

    efg = int(min(abc))
    print(efg)
  #  counts = int(min(klm))
  #  print(counts)

total(rs)
'''

# int(len(s))/2, for i in s[0: j]:

#
'''
s = 'babbaaa'
n = list(s)
print(n)
k = int(len(n))
b = []
count = 0

def fun():
    count = 0
    for i in range(0,k):
        if s[(k//2)] == n[i]:
            #print(i)
            b.append(i)
            #print(b)
            #print(len(b))
            if len(b) > 2:
                count += 1
                b.clear()
                print(n)
                #n.pop(i)
                #print(n)
                print(count)
'''



























