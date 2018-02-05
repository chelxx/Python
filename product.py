# Product Assignment

class Products(object):
    def __init__ (self, item_name, brand, price, weight, state):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.state = state

    def sell(self):
        print("Item Name: {}").format(self.item_name)
        print("Brand: {}").format(self.brand)
        print("Weight: {}").format(self.weight)
        if (self.state == "keep"):
            print("Price with tax: {}").format((self.price) * 1.10)
        if (self.state == "defective"):
            print("Status: Defective")
            print("Price: 0")
        if (self.state == "okay"):
            print("Status: For Sale")
            print("Price: {}").format((self.price)*0.80)
        print('\n')

def product_list():
    item1 = Products("Microwave", "KitchenAid", 100,  "20 lbs",  "keep").sell()
    item2 = Products("Table", "IKEA", 200,  "50 lbs", "defective").sell()
    item3 = Products("Blocks", "LEGO", 300, "10 lbs", "okay").sell()

product_list()

# WIP