# Stock management program using 2 classes (1 with inherited traits). Read and writes to a text file.
# Dear Marker, I'll be adding to this along with a GUI, i'm falling behind, but will update with a table as suggested
# at the end of the course

class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        self.code = code
        self.product = product
        self.cost = cost
        count = 0
        print(self.code)
        print('Product\t\t\t\t£Cost')

        for i in cost:
            print(f'{self.product[count]}\t\t\t£{self.cost[count]}\n')
            count += 1

    def get_quantity(self):
        self.product = product
        self.quantity = quantity
        count = 0
        for i in quantity:
            print(f'Product {count + 1}: {self.product[count]}\t\t\t\t\tQuantity: {self.quantity[count]}')
            count += 1

    def __str__(self):
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'


class Functions(Shoes):

    def read_shoes_data():  # takes IO from text file and appends to a list
        file = open('inventory.txt', 'r')

        inv = file.read()
        inv = inv.replace('\n', ',')  # removes \n and replaces with 'comma' .
        inv = inv.split(',')  # convert to list, split at ,
        count = 0

        for i in inv:
            output = i
            soutput.append(output)
            count += 1
            # print(output)

    def search_shoe(self):

        while True:
            code = input('Enter the product code ')
            code = code.upper()
            try:
                codey = self.code.index(code)
                if code in self.code:  # if object contains entered UPRN
                    print(self.country[codey])
                    print(self.product[codey])
                    print(self.cost[codey])
                    print(self.quantity[codey])
                    break

            except ValueError:

                print('Sorry, that product is not in the system')

                break

    def value_per_item(self):

        tracker = 0
        loop = 1
        while loop <= len(self.code):
            cost = int(self.cost[tracker])
            quantity = int(self.quantity[tracker])
            product = self.product[tracker]
            # value = cost * quantity
            value = f' The Value of {product} is R {cost * quantity}'
            tracker += 1
            loop += 1
            print(value)

    def highest_quantity(self):

        self.quantity = [int(x) for x in self.quantity]  # List comprehension as defined as str above

        q = self.quantity
        qmax = max(q)
        for_sale = self.product[q.index(qmax)]
        print(f'{for_sale} has a stock level of {qmax} and is now on sale')

    def restock(self):
        self.quantity = [int(x) for x in self.quantity]  # List comprehension as defined as str above

        q = self.quantity
        qmin = min(q)
        for_sale = self.product[q.index(qmin)]
        print(f'{for_sale} has the lowest in stock with {qmin} in storage')

        restock = 'yes'  # input('Would you like to restock this item? Yes or No ')
        restock = restock.upper()

        if restock == 'YES':

            file = open('inventory.txt', 'w')

            amount = int(input('How much are you ordering? '))
            self.quantity[q.index(qmin)] = amount
            self.quantity = [str(x) for x in self.quantity]  # List comprehension reverts to string

            loop = 0
            for i in range(len(self.code)):  # todo add header etc

                while loop < 1:
                    header = f'country,code,product,cost,quantity'
                    file.write(header)
                    break

                country = self.country[loop]
                code = self.code[loop]
                product = self.product[loop]
                cost = self.cost[loop]
                quantity = self.quantity[loop]
                loop += 1

                output = f'\n{country},{code},{product},{cost},{quantity}'

                # output = "".join(output)
                print(output)

                file.write(output)

                print(type(output))
                print(loop)

    def capture_shoe():
        file = open('inventory.txt', 'a')
        a = input('What country will this be based in? ')
        b = input('Enter the UPRN ')
        b = b.upper()
        c = input('What is the name of the product? ')
        d = input('Enter the price (whole numbers only) ')
        e = input('How many shoes will be brought into the warehouse? ')
        output = f'\n{a},{b},{c},{d},{e}'

        file.write(output)
        file.close()

    def view_all(self):
        loop = 0
        for i in range(len(self.product)):
            print(f'Country: {country[loop]}\t Code: {code[loop]}\t Product: {product[loop]}\t Cost: {cost[loop]}'
                  f'\t Quantity: {quantity[loop]}\n')
            loop += 1


while True:
    """Background Code. Gets info from text file to use for functions"""

    soutput = []  # list initially takes lines from text file.

    Functions.read_shoes_data()
    country = soutput[5::5]  # starts from index 5 as line prior is the headers
    code = soutput[6::5]
    product = soutput[7::5]
    cost = soutput[8::5]
    quantity = soutput[9::5]
    count = 0

    shoes = []

    for i in quantity:  # declaring attributes from list above. appends to 'shoes[]', which is the basis of this program
        a = country[count]
        b = code[count]
        c = product[count]
        d = cost[count]
        e = quantity[count]
        output = Shoes(a, b, c, d, e)
        Shoes(a, b, c, d, e)
        shoes.append(Shoes(a, b, c, d, e))
        count += 1

    shoes = Functions(country, code, product, cost, quantity)  # for Value Function

    print(
        f'Main Menu\n1 - Get Shoe Cost\n2 - Get list of quantities\n3 - Search for shoe by code\n4 - Stock Value\n5 - '
        f'Largest quantity (sale)\n6 - Restock\n7 - View All\n8 - Add New Product')

    main_menu = input('Please select what you would like to do ')
    if main_menu == '1':
        Shoes.get_cost(shoes)

    elif main_menu == '2':
        Shoes.get_quantity(shoes)

    elif main_menu == '3':
        Functions.search_shoe(shoes)

    elif main_menu == '4':
        Functions.value_per_item(shoes)

    elif main_menu == '5':
        Functions.highest_quantity(shoes)

    elif main_menu == '6':
        Functions.restock(shoes)

    elif main_menu == '7':
        Functions.view_all(shoes)

    elif main_menu == '8':
        Functions.capture_shoe()

    elif main_menu == '9':
        print('Goodbye')
        break

    else:
        print('Sorry, that is not an option')
        continue
