#📘 Standard Problem Statement

# Question:
# Write a Python function that takes an integer as input and returns the reverse of the number.

# If the number is negative, the reversed number should also be negative.

# Do not use built-in string reversal methods.

# Use arithmetic operations to reverse the digits.

def rev(num):
  neg = 1
  if (num < 0):
    neg = -1
    num = abs(num)
    
  temp = 0
  while(num > 0):
    rem = num % 10
    temp = temp * 10 + rem
    num = num // 10
    
  
  temp = temp * neg
  return temp
  
print(rev(-123))