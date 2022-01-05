
m = int(input()) #Номер столбца
n = int(input()) #Номер строки 

if (m>8) or (n>8) or (n<0) or (m<0):
    print('nonsence')
   

if m%2 == n%2 :
    print ('белая')
else:
        print ('чёрная')
        
