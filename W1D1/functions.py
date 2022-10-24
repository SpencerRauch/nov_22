#Functions 

#repeatable set of instructions that run when called. Functions can take an input, functions always return something (even if it's nothing)

"""
def function_name(parameter_1,parameter_2):
    #logic
    return 

"""

def multiply(num_1, num_2=5):
    print( num_1 * num_2 )
    # return num_1 * num_2


# print(200)
multiply(320)
# print(multiply(150,230))
# print(multiply(160,2560))
# print(multiply(190,2560))
# print(multiply(180,260))

def say_hello(name,times):
    for i in range(times):
        print("Hello " + name)

say_hello("Bob", 9)
say_hello(times=100,name="Steve") # this one caused an error because of a type mismatch #no longer an error with named args
# a function call is replaced by what the function returns