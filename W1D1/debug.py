def multiply(num_list, num):
    for i in range(len(num_list)):
        num_list[i] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)