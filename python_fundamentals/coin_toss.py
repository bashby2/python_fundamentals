# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
# Sample output should be like the following:
#
#           Starting the program...
#
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
head = 0
tail = 0
import random
for i in range (5001):
    flip = random.randint(0, 1)
    if flip == 0:
        head = head + 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)
    elif flip == 1:
        tail = tail + 1
        print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)
    else:
        print "Opps, something went wrong."
