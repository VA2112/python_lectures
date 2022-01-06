
x = int(input())
A = ['']*x

for i in range (x):
    A[i]=str(input())

for i in range (x):
    if i%2 == 0:
        print(A[i])
