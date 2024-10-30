class Cart:
    def __init__(self,name,price,description,quantity) -> None:
        self.name = name
        self.price = price
        self. description = description
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Your Shopping Cart Contains:\nCommodity : {self.name}\nPrice : {self.total_price()}\nCommodity Description : {self.description}\nQuantity : {self.quantity}"