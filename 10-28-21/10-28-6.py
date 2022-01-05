
b = int(input())

def is_prime(b):
    for i in range (2,1000):
        if b%i != 0:
            return True
            break
        else:
            return False
           

print (is_prime(b))
