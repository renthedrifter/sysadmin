# this is a special method because python calls __init__ automatically when you create an object.
class Student:
    def __init__(self, name):
        self.name = name

# other methods

#movies = ['Matrix', 'rush hour']
#print(len(movies))
#print(movies.__class__) # if you run this it'll output <class 'list'>.

# anything you can do in a list, you can do in their own classes.

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self): # all methods need self.
        return len(self.cars)

    def __getitem__(self, i): # the i is index.
        return self.cars[i]

    def __repr__(self): # prints out a string representing the object.
        return f'Garage with {len(self)} cars.'

#    def __str__(self): # returns something the user might want to read.
#        return f'Garage with {len(self)} cars.'

# if you're going to use one of repr or str, use repr. 

ford = Garage()
ford.cars.append('fiesta')
ford.cars.append('bronco')

print(ford)

#print(ford[0]) # Garage.__getitem__(ford,0)

# you can use for only when you have the len and getitem methods defined.

#for car in ford:
#    print(car)
