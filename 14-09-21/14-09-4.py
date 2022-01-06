
x = int(input())
fiban = [0]*(x+1)
fiban[0] = 1 
for i in range(1, x+1):
    fiban[i] = fiban[i-1] + fiban[i-2]
    fiban[1] = 1
    print (fiban[i])

print (fiban[x])
