# objects hold data and actions for the data, i.e. calculating average.
# normally in python the value after class starts with a capital letter.
# anything within {} is a dictionary.

my_student = {
        'name': 'earthworm jim',
        'grades': [50, 60, 78, 98],
        'average': None # something here
        }        

# normally in methods, the first parameter is called "self".
# a method is a function that belongs to an object.
class Student:
    def __init__(self, new_name, new_grades): # functions that start and end with two _ are called dunder functions.
        self.name = new_name # when we define a variable inside an object, that variable is now a property.00
        self.grades = new_grades

    def average(self):
        return sum(self.grades) / len(self.grades) # the len grabs all of the vaules in grades.

student_one = Student('earthworm jim', [50, 60, 78, 98]) # to create an object in python, we call the class i.e. Student.
student_two = Student('peter puppy', [73, 90, 83, 87])

#print(student_two.name)
#print(student_one.name)

print(student_one.average())
#print(Student.average(student_one)) #when you call line 25 this is what's going on in the background. Either will work.
