def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  total_bill = food_bill + electricity_bill + internet_bill + rent
  #return total_bill  
  print(total_bill)
  if budget < total_bill:
      return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# expected result: print False
#print(over_budget(80, 20, 30, 10, 30))
#expected result: print True