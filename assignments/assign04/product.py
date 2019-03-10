class Product:
    
    # this object has an ID, name,
    # price per item, and quantity purchased
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_total_price(self):
        # price is the cost of the item * the number of items 
        return self.price * self.quantity
    
    def display(self):
        print("{} ({}) - ${:.2f}" .format(self.name, self.quantity, self.get_total_price()))
        