'''
S = 'BAAABAB'
M = []
M[:0] = S
k = len(S)
count = 0

for j in range(len(M)):
    if M[j] == 'B':
        M[j] = 2
    if M[j] == 'A':
        M[j] = 1
print(M)

'''




'''
for i in range(0,4):
    if M[i] == 'B' and M[i+1] == 'A':
        del M[i]
        print(M)



for i in M:
    if M[0] == 'B' and M[1] == 'A':
        del M[0]
print(M)

if M[0].lower() == 'b':
    del M[0]
    count = count + 1
    print(count)'''

''''
for t in range(0, 4):
    if int(M[t]) > int(M[t]):
        del M[t]
print(M)

'''


