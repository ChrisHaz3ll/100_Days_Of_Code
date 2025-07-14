
#function add, as many numbers as want, add together all numbers, return total sum

def add(*args): #any number of positional arguments
    return sum(args) #args stored as Tuple... can be iterated through

result = add(3,5,8,10,23)
print(result)


def calculate(n, **kwargs): #any number of keyword arguments
    # kwargs stored as dictionary, keyword is key, arg is value
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make') #if key doesn't exist, will return None instead of error
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')

my_car = Car(make='Nissan')
print(my_car.model)