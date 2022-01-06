
x = int(input())
B = ['']*x

for i in range (x):
    B[i]=int(input())

for i in range (x):
    if B[i]%2 == 0:
        print(B[i])

