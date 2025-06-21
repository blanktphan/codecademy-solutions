# Pizza toppings and prices (parallel lists)
toppings = ['pepperonil', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

# Count how many pizzas cost $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Get total number of pizza types
num_pizzas = len(toppings)
print('We sell '+ str(num_pizzas) + " different kinds of pizza!")

# Combine prices and toppings into nested list
pizza_and_prices = [[2, 'pepperonil'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
print(pizza_and_prices)

# Sort by price (first element in each sublist)
pizza_and_prices.sort()

# Get cheapest and most expensive pizzas
cheapest_pizza = pizza_and_prices[0]  # First item after sorting
priciest_pizza = pizza_and_prices[-1]  # Last item

# Remove the most expensive pizza
pizza_and_prices.pop()

# Add new pizza to menu
pizza_and_prices.append([2.5, "peppers"])

# Get the three cheapest pizzas using slicing
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)