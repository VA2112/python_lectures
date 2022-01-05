#Начальная координата
m1 = int(input())
n1 = int(input())
#Конечная координата
m2 = int(input())
n2 = int(input())

if ( (m1-1 == m2) or (m1+1 == m2) ) and ( (n1+2 == n2) or (n1-2 == n2) ) or( (n1-1 == n2) or (n1+1 == n2) ) and ( (m1+2 == m2) or (m1-2 == m2) ) :
     print('YES')
else:
    print ('NO')

    
 
