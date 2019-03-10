from product import Product

class Order:
    
    def __init__(self):
        self.id = ""
        self.products = []
        
    def get_subtotal(self):
        sub_total = 0
        for product in self.products:
            sub_total += product.price * product.quantity
        return sub_total
    
    def get_tax(self):
        return 0.065 * self.get_subtotal()
    
    def get_total(self):
        return self.get_tax() + self.get_subtotal()
    
    def add_product(self, product):
        self.products.append(product)
    
    def display_receipt(self):
        print("Order: {}" .format(self.id))
        count = 1
        for product in self.products:
            product.display()
            # displaying the two decimals by using {0:.2f}
            # came from the website:
            # https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
        print("Subtotal: ${0:.2f}" .format(self.get_subtotal()))
        print("Tax: ${0:.2f}" .format(self.get_tax()))
        print("Total: ${0:.2f}" .format(self.get_total()))
        
        
        
    
    