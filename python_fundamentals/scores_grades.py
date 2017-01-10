# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is-generated, your program should display what the grade is for a particular score. Here is the grade table:

for i in range (1,10):
    grade = input("Enter grade: ")
    if grade >= 90:
        print "Score: {}; Your grade is A".format(grade)
    elif grade >= 80:
        print "Score: {}; Your grade is B".format(grade)
    elif grade >= 70:
        print "Score: {}; Your grade is C".format(grade)
    elif grade >= 60:
        print "Score: {}; Your grade is D".format(grade)
    elif grade < 60:
        print "Score: {}; Your grade is F".format(grade)
    elif grade == exit():
        print "Good bye!"
        break
    else:
        print "Please enter a number from 0 to 100"
    i = i + 1
print "End of program. Good bye!"
