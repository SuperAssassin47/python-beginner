# collecting name of file and storing it inside a variable
filename = "ex15_sample.txt"

# creates a file object to open the above file by calling the designated variable; filename
file = open(filename)

# returns a response message, stating the file object they created to open their txt file.
print(f'Your file is: {filename}')

# reads the contents of the file object
print(file.read())

# asks the user to re-type the name of their file on the line
print(f'Type your file here: ')

# indicates where the user should enter the name of their file and saves the response to a variable
txt = input('-> ')

# re-opens the file again from the response stored in the 'txt' variable above
file2 = open(txt)

# finally, this reads through the file again, showing the user what the contents of the file is.
print(file2.read())