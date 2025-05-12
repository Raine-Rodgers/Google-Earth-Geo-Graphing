a1_list = [10, 20, 30, 40, 50]  # Example inputs
target_min = 0.00050  # New target min
target_max = 0.00250  # New target max

a1_min = min(a1_list)
a1_max = max(a1_list)

# Normalize a1 values to [0,1]
a1_normalized = [(x - a1_min) / (a1_max - a1_min) for x in a1_list]

# Rescale normalized values to [target_min, target_max]
scaled_values = [x * (target_max - target_min) + target_min for x in a1_normalized]

# Output the scaled values and the average b1 multiplier
print("Scaled values:", scaled_values)