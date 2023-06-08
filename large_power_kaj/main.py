def large_power(base, exponent):
  summation = base **exponent
  #return summation
  print(summation)
  if summation > 5000:
      return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
#print(large_power(2, 12))
# should print False