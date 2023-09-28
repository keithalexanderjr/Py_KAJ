# Code Challenge: Max Number
# By Keith Alexander Jr.

def max_num(num1, num2, num3):
  if (num1 > num2) and (num1 > num3):
    return num1
  elif (num2 > num1) and (num2 > num3):
    return num2
  elif (num3 > num1) and (num3 > num2):
    return num3
  else:
    return "It's a tie!"

# Uncomment these function calls to test the max_num function:
print(max_num(-10, 0, 10))
# Result: print 10
print(max_num(-10, 5, -30))
# Result: print 5
print(max_num(-5, -10, -10))
# Result: print -5
print(max_num(2, 3, 3))
# Result: print "It's a tie!"