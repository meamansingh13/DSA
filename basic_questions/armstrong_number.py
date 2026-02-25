from count_digits import count_dig

def arms(num):
    dig = count_dig(num)
    temp, sum = num, 0
    while(dig>0):
        rem = num % 10
        num = num // 10
        sum = sum + rem ** 3
        dig = dig - 1

    return temp == sum

print(arms(153))