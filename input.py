import os

# Allows you to prompt the user for an integer input between a lower and upper bound
def user_input_integer(prompt, lower_b, upper_b):
    value = -1
    while value == -1:
        print("%s between %d - %d: " % (prompt, lower_b, upper_b))
        value = int(input())
        if value >= lower_b and value <= upper_b:
            return value
        else:
            value = -1

# Allows you to prompt the user for a filename (string input) and returns the path providing the file exists
def user_input_filename(prompt):
    value = ""
    while value == "":
        print("%s: " % prompt)
        value = input()
        if os.path.isfile('./images/' + str(value)):
            return './images/' + str(value)
        else:
            print("Invalid file name! (ensure the photo is in the images folder)")
            value = ''