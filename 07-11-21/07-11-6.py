#Вводятся координаты начальной клетки
m1 = int(input())
n1 = int(input())
#Вводятся кординаты конечной клетки
n2 = int(input())
m2 = int(input())

if ((m1 == m2) and (n1 != n2)) or ((n1 == n2) and (m1 != m2)):
    print('YES')
else:
        print('NO')

# m- строки, n - столбцы
