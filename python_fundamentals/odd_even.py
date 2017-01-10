# Create a function that counts from 1 to 2000. As it loops through each number, have your program generate the number and specify whether it's an odd or even number.

for i in range (1, 2001):
  if i % 2 != 0:
      print "Number is {}. The number is odd".format(i)
  else:
      print "Number is {}. The number is even.".format(i)
