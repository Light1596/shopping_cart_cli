
---

# Shopping Cart CLI Application

This is a simple command-line interface (CLI) application that allows users to browse available products by category, select items, specify quantities, and add them to a shopping cart. The application reads product information from a JSON file (`inventory.json`) and uses the `Cart` class from `brain.py` to manage and display the selected items.

## Features

- **Category Selection**: Users can browse products categorized by types.
- **Item Selection**: Users choose specific items within a category.
- **Quantity Input**: Users specify the quantity of the selected item.
- **Error Handling**: Robust handling for invalid categories, items, and quantities.
- **Cart Summary**: A final output displaying item details, total price, and quantity.

## Prerequisites

- **Python 3.x**: Ensure Python 3.x is installed.
- **JSON Inventory File**: `inventory.json` must be in the same directory as the script and contain the inventory data in valid JSON format.

## Installation and Setup

1. Clone this repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Ensure you have an `inventory.json` file with a structure similar to:
    ```json
    {
        "Cooking": [
            {
                "item": "Cooking Oil",
                "Price": 750,
                "Description": "Natural Coconut oil"
            },
            {
                "item": "Flour",
                "Price": 200,
                "Description": "All-purpose wheat flour"
            }
        ],
        "Snacks": [
            {
                "item": "Potato Chips",
                "Price": 100,
                "Description": "Salted potato chips"
            }
        ]
    }
    ```

3. Ensure `brain.py` is present in the same directory as `main.py`. The `brain.py` file should contain the following `Cart` class:

    ```python
    class Cart:
        def __init__(self, name, price, description, quantity) -> None:
            self.name = name
            self.price = price
            self.description = description
            self.quantity = quantity

        def total_price(self):
            return self.price * self.quantity

        def __str__(self):
            return f"Your Shopping Cart Contains:\nCommodity: {self.name}\nPrice: {self.total_price()}\nCommodity Description: {self.description}\nQuantity: {self.quantity}"
    ```

## Usage

1. **Run the Program**:
    ```bash
    python main.py
    ```

2. **Instructions**:
   - The program will display categories of products. Select a category by typing its name.
   - Choose an item within the selected category.
   - Enter the desired quantity of the item.
   - The program will display a summary of the item added to the cart.

3. **Example**:
    ```
    Categories of products available:
    - Cooking
    - Snacks
    Please choose one: Cooking
    Items available in Cooking category are as follows:
    - Cooking Oil
    - Flour
    Choose an item from the ones available: Flour
    What quantity of Flour do you want?: 2

    Your Shopping Cart Contains:
    Commodity: Flour
    Price: 400
    Commodity Description: All-purpose wheat flour
    Quantity: 2
    ```

## Error Handling

The application includes handling for:
- **Missing or Malformed JSON Files**: Alerts if `inventory.json` is missing or improperly formatted.
- **Invalid Category and Item Selection**: Notifies the user if they select a nonexistent category or item.
- **Invalid Quantity Input**: Prompts the user to enter a positive integer for quantity.

## License

This project is licensed under the MIT License.

---