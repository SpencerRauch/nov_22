#LOOPS!

#FOR
# for ___ in ____:

#Blank #1 -- iterative variable -- will mean different things for different datatypes that we iterate over
#Bland #2 -- sequence or collection that you are iterating over

#range(start,stop,step)
"""
start -- optional, defaults to 0, inclusive
stop -- required, exclusive
step -- increment value -- can positive or negative
"""
# for i in range(40,-2,-2):
#     print(i)

#looping over a list the iterative variable will represent each element of the list in turn

foods = ['pizza', 'nachos', 'burger', 'tacos', 'orange chicken', 'potatos', 'sushi']

# for one_food in foods:
#     print(one_food)
#     one_food = "toast" #this does not work

# # print(foods)
# for i in range(len(foods)):
#     print(foods[i])
#     foods[i] = "toast" #this will work because we're accessing by index

# print(foods)

#looping over dictionaries

cat1 = {
    'name': 'Cinnamon',
    'age':2,
    'color': 'orange'
}
cat2 = {
    'name': 'Meow',
    'age':2,
    'color': 'black'
}

# for key in cat1:
#     print(f"The key is {key} the value is {cat1[key]}")

# for key,val in cat1.items():
#     print(f"The key is {key} the value is {val}")


list_of_cats = [cat1,cat2]
name = list_of_cats[1]['name']

for cat_dict in list_of_cats:
    for key in cat_dict:
        print(f"The key is {key} the value is {cat_dict[key]}")

#WHILE
"""
while(condition):
    pass

"""

x = 5
while (x > 0):
    print(x)
    x -= 1
