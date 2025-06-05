# collects target file and stores in a variable, orig_file
orig_file = "dummy.txt"

# function to print everything from target file
def print_all(f):
    print(f.read())

# function to rewind to a certain point in the target file based on the read head
# the 0 signifies the beginning of the target file. Or line 0 of the target file.
def rewind(f):
    f.seek(0)

# function to output certain lines from the target file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the target file and stores the data in a variable
new_file = open(orig_file)

# response message to show the user the script is printing everything from the target file
print("I am going to print the whole file:\n")

# calling the print_all() function
print_all(new_file)

# response message to show the user the script is rewinding to a byte in the target file
print("Now I am going to rewind to the beginning of the file:\n")

# calling the rewind() function
rewind(new_file)

# response message to show the user the script is printing specific lines from the target file
print("Now I am going to only print four lines:\n")

# starting on line 1 of the target file and assigning to a variable, current_line
current_line = 1

# calling the print_a_line() function with necessary arguments within its parentheses
print_a_line(current_line, new_file)

# incrementing current_line by 1 to show the user script is adding a second line
current_line = current_line + 1

# calling the same function again with necessary parameters (arguments)
print_a_line(current_line, new_file)

# incrementing current_line by 1 again to output another line
current_line = current_line + 1

# calling the same function again with the same parameters (arguments)
print_a_line(current_line, new_file)

# incrementing current_line by 1 again, outputting another line
current_line = current_line + 1

# calling the same function again with the same parameters (arguments)
print_a_line(current_line, new_file)

# incrementing current_line by 1 again, outputting another line
current_line = current_line + 1

# calling the same function again with the same parameters (arguments)
print_a_line(current_line, new_file)
