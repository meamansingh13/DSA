# 📘 Standard Problem Statement

# Question:
# Write a program to count the number of digits present in a given integer.

def count_dig(num):
  count = 0
  while(num > 0):
    num = num // 10
    count = count + 1
  return count

print(count_dig(344))