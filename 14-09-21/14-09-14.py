
M = [1]
C = 0 
i = 0
while M[i] != 0:
    i +=1
    M.insert(i,(int(input())))

max_index = 0

for i in range(len(M)):
    if M[i] == M[i-1]:
        C += 1
    else:
        if C > max_index:
            max_index = C
        C = 0

print (max_index + 1)
        
