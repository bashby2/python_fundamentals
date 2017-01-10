# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

a = [2,4,10,16]
b = 5
d = []
def multiply(a, b):
    for i in range(0, len(a)):
        c = b * a[i]
        d.append(c)
        i = i + 1
    return d
result = multiply(a, b)
print result
