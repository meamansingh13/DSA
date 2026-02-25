def divisor(num):
    ans = []
    for i in range(1, int(num ** 0.5)+1):
        if(num % i == 0):
            ans.append(i)
            if(i != num // i):
                ans.append(num // i)
    ans.sort()
    return ans

print(divisor(36))