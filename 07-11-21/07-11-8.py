#длинна некоторых бортов N и M
N = int(input())
M = int(input())
#Расстояние до большого борта
x = int(input())
#Расстояние до маленького борта
y = int(input())

if M>N:
    big = M
    small = N
else:
    big = N
    small = M

if x > big//2:
    x = big - x

if y > small//2:
    y = small - y

if x>y:
    print(y,"м")
else:
    print(x,"м")
    
