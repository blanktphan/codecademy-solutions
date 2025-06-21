hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]  # Hair salon services

prices = [30, 25, 40, 20, 20, 35, 50, 35]  # Prices for each hairstyle

last_week = [2, 3, 5, 8, 4, 4, 6, 2]  # Number of each service sold last week

total_price = 0  # Initialize accumulator

# Sum all prices using for loop
for price in prices:
  total_price += price

# Calculate average price
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

# Create discounted price list ($5 off each)
new_prices = []
for price in prices:
  new_prices.append(price - 5)

print(new_prices)

total_revenue = 0  # Initialize revenue accumulator

# Calculate total revenue (price × quantity sold)
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print('Total Revenue: '+ str(total_revenue))

# Calculate daily average from weekly total
average_daily_revenue = total_revenue / 7

# Find hairstyles under $30 after discount
cuts_under_30 = []
for i in range(0, len(new_prices)):
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])

print('Under 30$ :'+ str(cuts_under_30))