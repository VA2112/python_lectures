#Сначала вводится число, потом степень

a = int(input())
n = int(input())

def power(a,n):
    m = a
    for i in range(n):
            a *= m
    if n >0:
        return (a)
    elif n <0:
        return (1/a)
    elif n == 1:
        return (n-1)

print(power(a,n-1))
