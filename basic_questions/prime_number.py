def prime(num):
    for i in range(2, num // 2):
        if(num % i == 0):
            return False
    return True

print(prime(7))