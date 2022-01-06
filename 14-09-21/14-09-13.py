
M = [1]
C = 0 
i = 0
while M[i] != 0:
    i +=1
    M.insert(i,(int(input())))

sorted(M)

max_index = M[1]

for i in range (1,len(M)):
    if M[i] == M[1]:
        C += 1

print (C)
