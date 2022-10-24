print("Hello")

# This is my comment 

"""
I can type whatever I want
on multiple lines!
"""

snake_case = "All lower case, separated by underscores"
GLOBAL_VAR = "All caps"
#class names will be pascal case ie HumanClass

#Datatypes

#Primitive

#number
integer = 6
float_num = 6.8

#strings
string_one = "A collection of characters"
format_str = f"Now we can put variables in this {integer}"
concat_str = "Concat var" + str(integer)

print(concat_str)
print(format_str)

#booleans
# True or False
bool1 = True
bool2 = False


#Composite
#list -- what we call arrays in js, a collection of elements accessed by index
list = [1,2,3,4,5,6,100,100]
#       0 1 2 3 4 5  6   7
print(list[3])
list[3] = 100
print(list[3])

#list functions
len(list) #returns the length of the list (.length in js)
min(list) # minimum
max(list) # highest value

#list methods
list.append(393) #add a value to the end of the list
list.remove(100) #removes the specified value
popped = list.pop(1) #removes a value at an index
list.sort(reverse=True)
print(list)


#dictionaries
# a sequence of KEY VALUE PAIRS
# unindexed 
# keys are all strings
dog_dict = {
    'name': 'Wiley',
    'age': 4,
    'breed': "Chihuahua / Pomeranian Mix"
}

print(dog_dict['name'])
# dog_dict['color'] = "Orangish tan"
print(dog_dict)
# print(dog_dict['color'])

# if "color" in dog_dict:
#     print(dog_dict['color'])
# else:
#     print("Key not found")
#     dog_dict['color'] = "Default color"

#removing from dict
# del dog_dict['breed']
# color = dog_dict.pop('color')
# dog_dict.clear()


#tuples
#immutable list CANNOT BE CHANGED
tuple = (1,2,3,4,5)
print(tuple[0])
# tuple[0] = 4958498 THIS CAUSES AN ERROR


#conditional running code based on whether or not a statement is true
#if
#else
#elif <--- this is the one weird part of python to me

x = 8
if x == 5:
    print("x is 5")
elif x > 5:
    print("greater than 5")
else:
    print("less than 5")

"""
== not the ===
None instead null
not instead of ! 
or instead of ||
and instead of &&
is vs ==
    is used to check if both operands refer to the same object
    
"""