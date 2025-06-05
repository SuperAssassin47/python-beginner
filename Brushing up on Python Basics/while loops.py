# declaring variable and assigning 0 to it.
i = 0

# creating an empty list and assigning the list to variable integers.
integers = []

# declaring the While loop. This will continue as long as the condition (i < 6) is true.
while i < 6:

    # outputting a formatted string using String Concatenation
    print(f'At the top i is {i}')

    # appending the new number to the integers list
    integers.append(i)

    # incrementing i by 1
    i += 1

    # printing the list as it is, using the integers variable
    print('Numbers is now: ', integers)

    # outputting a formatted string using String Concatenation
    print(f'At the bottom i is {i}')

# printing all the integers stored in the list
print("The integers: ")

# for-loop to iterate (loop) through the integers list, assigning them to a declared variable and outputting them to the
# console
for number in integers:
    print(number)
