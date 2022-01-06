#Введём последовательность
Q = [1]
S = 0 
i = 0
while Q[i] != 0:
    i +=1
    Q.insert(i,(int(input())))


for i in range (1,(len(Q)-2)):
    if (Q[i]>Q[i-1]) and (Q[i]>Q[i+1]):
        S += 1
        

print(S)
