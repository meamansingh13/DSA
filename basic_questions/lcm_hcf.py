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