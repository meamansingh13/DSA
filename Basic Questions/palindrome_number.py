# 📘 Standard Problem Statement

# Question:
# Write a program to check whether a given integer is a palindrome or not.

# A number is called a palindrome if it reads the same forward and backward.

def palindrome(num):
  if (num < 0):
    return False
  original_num = num
  temp = 0
  while(num > 0):
    rem = num % 10
    temp = temp * 10 + rem
    num = num // 10
    
  return temp == original_num
  
print(palindrome(121))