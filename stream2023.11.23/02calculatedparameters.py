class Podarok():
    def __init__(self, name_of_class, children_amount, candy_amount):
        self.name_of_class = name_of_class
        self.children_amount = children_amount
        self.candy_amount = candy_amount
        self.for_one = candy_amount/children_amount
        
podarok1 = Podarok("1А", 20, 400)
print(podarok1.for_one)
        