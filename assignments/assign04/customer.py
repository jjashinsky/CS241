from order import Order

class Customer:
    
    # this object has an ID, name,
    # and an order. 
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = [] # this will store the objects,
                         # order(), for the customer
        
    def get_order_count(self):
        # counts the number of orders the customer has
        return len(self.orders)
    
    def get_total(self):
        total = 0
        # this will go through the list and add
        # the totals from each order
        for order in self.orders:
            total += order.get_total()
        return total
    
    def add_order(self, order):
        self.orders.append(order)
    
    def display_summary(self):
        print("Summary for customer '{}':" .format(self.id))
        print("Name: {}" .format(self.name))
        print("Orders: {}" .format(self.get_order_count()))
        print("Total: ${0:.2f}" .format(self.get_total()))
    
    def display_receipts(self):
        print("Detailed receipts for customer '{}':" .format(self.id))
        print("Name: {}" .format(self.name))
        
        for order in self.orders:
            print()
            order.display_receipt()
            
        
    