# you can use inheritance to remove duplication.  



class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student): # WorkingStudent is now a child of Student.
    def __init__(self, name, school, salary):
        super().__init__(name, school) # super is the parent class, in this case Student.
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 40.0

# don't need these because of inheritance. 
#    def average(self):
#        return sum(self.marks) / len(self.marks)

earthworm = WorkingStudent('EWJ', 'MIT', 15.50)
print(earthworm.salary)
print(earthworm.weekly_salary())
