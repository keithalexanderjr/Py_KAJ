def in_range(num, lower, upper):
  if (num >= lower and num <= upper):
    return True
  else:
    return False

# Function calls to test in_range function:
# Test 1:
print(in_range(10, 10, 10))
# Expected Result: print True
# Test 2:
print(in_range(5, 10, 20))
# Expected Result: print False
