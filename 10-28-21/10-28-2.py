def bin_to_dec(digit):
    dlina = len(digit)
    chislo_dec=0
    for i in range(0, dlina):
        chislo_dec=chislo_dec+int(digit[i])*(2**(dlina-i-1))
    return chislo_dec
a=input("Введи двоичное целое число =")
print("Двоичное целое число", a, "соответсвует десятичному числу", bin_to_dec(a))

def bin(b):
    i = 0
    binar = ['1']
    while b>1:
        binar.append(str(b%2))
        b = b//2
        i += 1
    return("".join(binar))

print('Введите число в десятичной системе')

a = int(input())
print('Оно же в двоичной:',bin(a))
