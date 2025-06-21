weight = 41.5  # Package weight in pounds

# Ground Shipping - Calculate cost based on weight tiers
if weight <= 2:
  cost_ground = (weight * 1.5) + 20  # $1.50/lb + $20 flat rate
elif weight > 2 and weight <= 6:
  cost_ground = (weight * 3) + 20    # $3.00/lb + $20 flat rate
elif weight > 6 and weight <= 10:
  cost_ground = (weight * 4) + 20    # $4.00/lb + $20 flat rate
elif weight > 10:
  cost_ground = (weight * 4.75) + 20 # $4.75/lb + $20 flat rate

print('Ground Shipping $', cost_ground)

# Ground Shipping Premium - Fixed flat rate
cost_premium = 125  # Always $125 regardless of weight

print('Ground Shipping Premium $', cost_premium)

# Drone Shipping - Calculate cost based on weight tiers (no flat rate)
if weight <= 2:
  cost_drone = (weight * 4.5)   # $4.50/lb only
elif weight > 2 and weight <= 6:
  cost_drone = (weight * 9)     # $9.00/lb only
elif weight > 6 and weight <= 10:
  cost_drone = (weight * 12)    # $12.00/lb only
elif weight > 10:
  cost_drone = (weight * 14.25) # $14.25/lb only

print('Drone Shipping $', cost_drone)

# Compare all three options and find cheapest
if cost_ground < cost_drone and cost_ground < cost_premium:
    print(f"Ground Shipping is cheapest at ${cost_ground}")
elif cost_drone < cost_premium:
    print(f"Drone Shipping is cheapest at ${cost_drone}")
else:
    print(f"Premium Ground Shipping is cheapest at ${cost_premium}")