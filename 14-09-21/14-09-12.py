# Какие-то значения 
M = [1]
C = 0 
i = 0
while M[i] != 0:
    i +=1
    M.insert(i,(int(input())))

index_max = 0
max_index = 0

for i in range(len(M)):
    if M[i]>max_index:
        max_index = M[i]
        index_max = i

print (max_index,' ',index_max)
