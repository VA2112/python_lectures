#Длинна массива
x = int(input())
b = [0]*(x+1)
#Список чисел 

for i in range (x):
    b[i] = int(input())

for i in range (x):
    if (b[i]>=0 and b[i+1]>=0) or (b[i]<0 and b[i+1]<0):
        print(b[i],b[i+1])
        break
    
