''' QUESTION
Given the following class representing a Car, add a method ‘start engine’ that prints ‘Engine
started.’
c l a s s Car :
d e f i n i t ( s e l f , brand , model ) :
s e l f . brand = brand
s e l f . model = model
d e f d i s p l a y i n f o ( s e l f ) :
p r i n t ( f ”{s e l f . brand }{s e l f . model }” )
# Add t h e s t a r t e n g i n e method h e r e
# Example u s a g e :
my car = Car ( ’ Toyota ’ , ’ Camry ’ )
my car . d i s p l a y i n f o ( )
my car . s t a r t e n g i n e ( )
'''

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")

    def start_engine(self):
        print("Engine started.")

my_car = Car("Toyota", "Camry")
my_car.display_info()
my_car.start_engine()

''' OUTPUT
$ python3 p_car_class.py 
Toyota Camry
Engine started.
'''
