# Ввести в порядке возрастания 
M = [1]
C = 0 
i = 0
while M[i] != 0:
    i +=1
    M.insert(i,(int(input())))

for i in range(len(M)):
               if M[i] != M[i-1]:
                   C += 1

print (C-2)
