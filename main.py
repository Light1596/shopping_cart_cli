from brain import *
import json

try:
    with open("./inventory.json", 'r') as items_available:
        files = json.load(items_available)
except FileNotFoundError:
    print("Error: The inventory file was not found.")
    exit()
except json.JSONDecodeError:
    print("Error: The inventory file is not in a valid JSON format.")
    exit()

# Lists for storing information about items
prices = []
items = []
descriptions = []

# Display categories
print("Categories of products available:")
for category in files.keys():
    print(category)

# Get user input for category choice
user_category = input("Please choose one: ").title().strip()

# Check if category exists
if user_category not in files:
    print("Error: No such category available.")
    exit()

# Display items in the selected category
print(f"Items available in {user_category} category are as follows:")
for i in files[user_category]:
    print(i['item'])
    prices.append(i['Price'])
    items.append(i['item'])
    descriptions.append(i['Description'])

# Get user input for item choice
user_item_choice = input("Choose an item from the ones available: ").strip()
if user_item_choice not in items:
    print("Error: No such item available in the chosen category.")
    exit()

# Get the quantity and handle invalid input
try:
    index_of_choice = items.index(user_item_choice)
    item_quantity = int(input(f"What quantity of {user_item_choice} do you want?: "))
    if item_quantity <= 0:
        raise ValueError("Quantity should be a positive integer.")
except ValueError as e:
    print(f"Error: {e}")
    exit()

# Add selected item to the shopping cart
shopping_cart = Cart(user_item_choice, prices[index_of_choice], descriptions[index_of_choice], item_quantity)
print(shopping_cart)
