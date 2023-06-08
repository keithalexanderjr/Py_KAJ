hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

#number of last week sales for each item
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for item in prices:
  total_price = total_price + item
print("Total Price of Items: " + str(total_price))

#Average price of haircut
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

#Append all prices by 5 dollars
new_prices = [num - 5 for num in prices]
print(new_prices)

#revenue brought in last week
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " +  str(total_revenue))

#Average Daily Revenue
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#Special Customer Deal: Cuts under 30 dollars 
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]
print(cuts_under_30)
