# Product descriptions
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."


# Product prices
lovely_loveseat_price = 254.00
stylish_settee_price = 180.50
luxurious_lamp_price = 52.15

# Tax rate (8.8%)
sales_tax = .088

# Customer One variables
customer_one_total = 0  # Start with $0
customer_one_itemization = ''  # Empty receipt list

# Add Lovely Loveseat to order
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# Add Stylish Settee to order
customer_one_total += stylish_settee_price
customer_one_itemization += "\n" + stylish_settee_description

# Calculate tax on subtotal
customer_one_tax = customer_one_total * sales_tax

# Add tax to get final total
customer_one_total += customer_one_tax

# Print customer receipt
print('Customer One Items:' + customer_one_itemization)
print('Customer One Total:' + " " + str(customer_one_total))