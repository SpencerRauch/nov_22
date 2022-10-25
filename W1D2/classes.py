#OOP?
#Object Orientated Programming
# creating objects in our code using classes, attributes and methods
#grouping data and functionality together into one single entity, called an Object

dog_1 = {
    "name": "Spot",
    "age": 3,
    "breed": "Corgi"
}

dog_2 = {
    "name": "Mr Worldwide",
    "age": 34,
    "breed": "pitbull"
}





#What is a class?
#Blue print
class Dog:

    is_cute = True
    all_dogs = []

    # def __init__(self, data, roommate):
    #     self.name = data['name']
    #     self.age = data['age']
    #     self.breed = data['breed']
    #     Dog.all_dogs.append(self)
    #     self.roommate = roommate

    # def __init__(self, data, name):
    #     self.name = data['name']
    #     self.age = data['age']
    #     self.breed = data['breed']
    #     Dog.all_dogs.append(self)
    #     self.roommate = Human(name)

    def __init__(self, data, roommate = None):
        if roommate == None:
            print("This dog is a stray")
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']
        Dog.all_dogs.append(self)
        self.roommate = roommate

    def bark(self):
        print(f"{self.name} makes a loud bark at their roommmate {self.roommate.name}")
        return self

    def birthday(self):
        self.age += 1
        print(f"{self.name} gets a special bday treat! They are now {self.age} year(s) old")
        return self

    def __repr__(self):
        return f"{self.name} is a dog object {self.age} {self.breed}"

    @classmethod
    def every_dog_barks(cls):
        # if cls.is_cute:
        #     print("In a very cute manner,")
        for one_dog in cls.all_dogs:
            one_dog.bark()

    @staticmethod
    def years_to_dog_years(years):
        return years * 7

    @staticmethod
    def is_valid(data):
        if data['name'] == "":
            print("This is not okay")

class Human:
    def __init__(self, name) -> None:
        self.name = name

# dog_3 = Dog("Minnie", 4, "corgi")
# dog_4 = Dog("Max",4,"Great Dane")
branden = Human("Branden")
spencer = Human("Spencer")
dog_3 = Dog(dog_1)
dog_4 = Dog(dog_2, spencer)
# dog_4.roommate = spencer
dog_3.roommate = branden

# print(dog_3)
# print(dog_3.name)
# print(dog_4.name)

#What is an attribute?e
# a characteristic of our object, some piece of data we are tracking about our object
# ie breed, age, color for a dog

#What is a method?
# a function belonging to the class -- what our objects can do
# dog_3.bark().bark().bark().birthday().bark()
Dog.every_dog_barks()
print(Dog.all_dogs)
Dog.is_cute

#Classmethods
# affects things on a class level, no access to any one individual instance

#Staticmethods
# doesn't affect the class or the instance!