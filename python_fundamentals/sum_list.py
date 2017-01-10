#Sum list
#Create a program that prints the sum of all the values in the list:

a = [1, 2, 5, 10, 255, 3]
b = 0
for i in range (0, len(a)):
    b = b + a[i]
print b

#or using the built in sum function

a = [1, 2, 5, 10, 255, 3]
asum = (sum(a))
print asum
