# Advanced Code Challenge: Always False Code Challenge
# By Keith Alexander Jr.


def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# Expected Result: print False
print(always_false(-1))
# Expected Result: print False
print(always_false(1))
# Expected Result: print False
