# collecting the file and storing it in a variable for future reference
filename = "dummy.txt"

# response message that outputs to make it look like the user is talking to an AI engine
print(f'Hello! I am the File Truncator. I am going to truncate the file {filename}.')

# brief loading message that shows the user the script is opening the file in 'write' mode
print("OPENING SAID FILE....")

# opens and stores it in a variable called 'experiment'
experiment = open(filename, 'w')

# warning message that asks the user if they want to proceed or not
print("If you don't want me to truncate/empty this file, hit CTRL+C (^C) now") # DISCLAIMER: this is just for educational purposes only
print("Otherwise, hit ENTER or RETURN!!")

# prompt to indicate where the user should hit ENTER or RETURN to initiate the file truncation
input("?")

# loading message displays showing the user that the file is being truncated
print("BEGINNING FILE TRUNCATION....")
experiment.truncate()

# success message displays after the file has been truncated/emptied successfully
print("FILE TRUNCATION SUCCESSFUL!!")

# response message displays to ask user to enter 5 sentences
print("Now, I am going to ask you to enter five sentences below: ")

# user enters their 5 sentences of their choosing and stores each into five separate variables
line1 = input("Sentence 1 -> ")
line2 = input("Sentence 2 -> ")
line3 = input("Sentence 3 -> ")
line4 = input("Sentence 4 -> ")
line5 = input("Sentence 5 -> ")

# thank you message displays to show gratitude to the user
print("THANK YOU!!")

# response message to write the 5 sentences to the emptied (truncated) file
print("I am going to now write these to the truncated file! :D")

# loading message to show the user that the script is writing the 5 sentences to the file using relevant escape codes
print("WRITING TO FILE....")
experiment.write(line1)
experiment.write("\n")
experiment.write(line2)
experiment.write("\n")
experiment.write(line3)
experiment.write("\n")
experiment.write(line4)
experiment.write("\n")
experiment.write(line5)

# final success message displays showing the 5 sentences have been successfully written to the file
print("SUCCESS! Now the file has been written to. You can now safely close the file!")

# closing the file after its use
experiment.close()