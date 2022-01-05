print('вклад на срок')
years = int(input())

print('Сумма')
a = int(input())

def bank(years,a):
    i = 0
    for i in range (years):
        a += 0.1*a
    return (a)

print(bank(years,a))
