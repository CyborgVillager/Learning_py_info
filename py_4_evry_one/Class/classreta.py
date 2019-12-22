class RetailItem:
   #Ensure your customer has the proper information check your warehouse inv.
   #use our brand new syst called JA invtory mang!  -> will print this out soon
    def __init__(self, description, units, price):
        self.__item_description = description
        self.__units_in_inventory = units
        self.__price = price

    # The set_item_description method gets the item type.
    def set_item_description(self, description):
        self.__item_description = description


    def set_units_in_inventory(self, units):
        self.__units_in_inventory = units


    def set_price(self, price):
        self.__price = price


    def get_item_description(self):
        return self.__item_description


    def get_units_in_inventory(self):
        return self.__units_in_inventory


    def get_price(self):
        return self.__price



def main():

    inventory = make_list()
    print('Your product information:')
    display_list(inventory)



def make_list():
#  will work on making the list save the information
    item_list = []


    print('Enter data for your mechandise')
    for count in range(1, 4):
        # Get item data.
        print('Product amount ' + str(count) + ':')
        item = input('Product Name: ')
        units = float(input('Number of units in inventory: '))
        price = float(input('Enter price per item: '))
    print()

        # Creat new RetailItem and assign items variable.
    items = RetailItem(item, units, price)
        # Add items to list.
    item_list.append(items)

    return item_list

#Display the items information.
def display_list(item_list):
    for item in item_list:
        print(item.get_item_description())
        print(item.get_units_in_inventory())
        print(item.get_price())
        print()

main()