def absolute_value(a):
    return abs(a)


def gcd(a, b):
    a, b = absolute_value(a), absolute_value(b)
    if a == 0 and b == 0:
        return None
    elif b == 0:
        return a
    elif a == 0:
        return b
    elif a > b:
        return gcd(b, a % b)
    elif a < b:
        return gcd(a, b % a)


#  for i in range(1, max(a, b) + 1):
#      if a % i == 0 and b % i == 0:
#          common_divisor = i
#      else:
#          pass
#  return common_divisor

a = 33
b = 17
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")
