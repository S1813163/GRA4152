
"""
Implement a superclass Person. Make two classes, Student and Instructor, that inherit
from Person. A person has a name and a year of birth. A student has a major, and an
instructor has a salary. Write the class declarations, the constructors, and the _ _repr_ _
method for all classes. Supply a test program that tests these classes and methods.

"""
# Load package datetime to calculate age
import datetime

##
#  This module defines the Person superclass
#
class Person:
    ## Constructs a person where the inputs are name and year of birth
    #
    def __init__(self, name, yearOfBirth):
        self._name = name
        self._age = datetime.datetime.today().year - yearOfBirth
    
    ## Returns the name of the person
    #  @param the name to return
    #  @return returns the name of the person
    def name(self):
        return self._name

    ## Returns the age of the person
    #  @param the age to return
    #  @return returns the age of the person    
    def age(self):
        return self._age
    
    ## Gets a string representation of the person
    #  @return a string containing name and age of person
    def __repr__(self):
        return "The person is called " + str(self._name) + " and is " + str(self._age) + " years old"

##
#  This module defines the Student subclass
#        
class Student(Person):
    ## Constructs a student from the Person superclass where the inputs are name, year of birth and major
    #
    def __init__(self, name, yearOfBirth, major):
        super().__init__(name, yearOfBirth)
        self._major = major

    ## Returns the major of the student
    #  @param the major to return
    #  @return returns the major of the student        
    def major(self):
        return self._major

    ## Gets a string representation of the student
    #  @return a string containing name, age of student, and major
    def __repr__(self):
        return "The student is called " + str(self._name) + ", is " + str(self._age) + " years old, " + "and takes a major in " + str(self._major)

##
#  This module defines the Instructor subclass
#    
    
class Instructor(Person):
    ## Constructs a instructor from the Person superclass where the inputs are name, year of birth and salary
    #
    def __init__(self, name, yearOfBirth, salary):
        super().__init__(name, yearOfBirth)
        self._salary = salary

    ## Returns the salary of the instructor
    #  @param the salary to return
    #  @return returns the salary of the instructor           
    def salary(self):
        return self._salary

    ## Gets a string representation of the instructor
    #  @return a string containing name, age of instructor, and salary    
    def __repr__(self):
        return "The instructor is called " + str(self._name) + ", is " + str(self._age) + " years old, " + "and has a salary amounting to " + str(self._salary) + "USD"


# Tester program for the superclass and the subclasses
z = Person("Huey", 1980)
print(z)

x = Student("Dewey", 1993, "Quantitative Finance")
print(x)  

y = Instructor("Louie", 1963, 50000)
print(y)
