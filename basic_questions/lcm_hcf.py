# 📘 Standard Problem Statement

# Question:
# Write a program to find the HCF (Highest Common Factor) and LCM (Least Common Multiple) of two given integers.

# HCF is the greatest number that divides both numbers exactly.

# LCM is the smallest number that is divisible by both numbers.

def hcf(num1, num2):
  a = max(num1, num2)
  b = min(num1, num2)
  while (b != 0):
    rem = a % b
    a = b
    b = rem
  
  return a

def lcm(num1, num2):
  return (num1 * num2) // hcf(num1,num2) 

print(lcm(5,10))