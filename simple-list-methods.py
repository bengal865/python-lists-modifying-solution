# Create a shopping list
shopping_list = ["apples", "bread", "milk", "juice", "cookies"]

# Print the original list
print("Original shopping list:", shopping_list)

# Add an item using append
shopping_list.append("eggs")
print("\nShopping list after adding eggs:", shopping_list)

# Remove an item using remove
shopping_list.remove("cookies")  # Can cause errors if cookies isn't there
print("\nShopping list after removing cookies:", shopping_list)

# Check if an item exists (without removing it)
if "bread" in shopping_list:
  print("\nBread is still in the list.")
else:
  print("\nBread is not in the list.")

# Find the index of an item (useful for later removal or modification)
item_index = shopping_list.index("milk")
print(f"\nMilk is at index {item_index} in the list.")
