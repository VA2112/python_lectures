
m = int(input())
i = m//2
mms = 0
for i in range(m//2,2,-1):
    if (m%i == 0):
        mms = i
        
print (mms)


