
A = [1]
S = 0 
i = -1
b = 1
while b != 0:
    i +=1
    A.insert(i,(b))
    b = int(input())
    




B = [1]
S = 0 
i = -1
b = 1
while b != 0:
    i +=1
    B.insert(i,(b))
    b = int(input())

A.remove(1)
B.remove(1)

Sum = 0
C = [1]

if len(A) == len(B):
    for i in range (len(A)):
        Sum += A[i]*B[i]

print(Sum-1)
