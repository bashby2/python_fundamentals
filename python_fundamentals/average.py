# Create a program that prints the average of the values in the list:

a = [1, 2, 5, 10, 255, 3]
b = 0
for i in range (0, len(a)):
    b = b + a[i]
    b = b / len(a)

print b

# or using the built in sum function

a = [1, 2, 5, 10, 255, 3]
ave = (sum(a)) / len(a)

print ave
