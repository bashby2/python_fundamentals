# Part 1
# Create a function called  draw_stars() that takes a list of numbers and prints out  *.
def draw_stars(*args):
    for arg in args:
        star_count = " "
        for i in range (arg):
            star_count += "*"
        print star_count
draw_stars(1, 2, 2, 4)

# Part 2
# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
#
# For example:
#
#  x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(*args):
    for arg in args:
        star_count = ""
        if args is str:
            star_count = args[0].lower()
            for i in range (len(arg)):
                star_count += star_count
        elif args is int:
            for i in range (arg):
                star_count += "*"
        print star_count
draw_stars(4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith")

# y = [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
# def draw_stars2(my_list):
#     for item in my_list:
#         output = ''
#         if type(item) is int:
#             for i in range(item):
#                 output += '*'
#         elif type(item) is str:
#             first_letter = item[0].lower()
#             for i in range(len(item)):
#                 output += first_letter
#         print output
#
# draw_stars2(y)
