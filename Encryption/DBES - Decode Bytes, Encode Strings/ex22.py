# importing the sys module
import sys

# this is the command line argument handling.
script, input_encoding, error = sys.argv

# defining main() function and assigning three parameters (arguments)
def main(language_file, encoding, errors):
    # reading through each line of the language file and assigning to the 'line' variable
    line = language_file.readline()

    # if-statement to check if 'line' has any assigned values stored. If yes, the body of the if-statement will
    # return true and exit this block of code
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

# defining another function called print_line() and assigning three other parameters to it
def print_line(line, encoding, errors):
    # stripping the \n at the end of the 'line' string
    next_lang = line.strip()

    # DBES - 'Decode Bytes, Encode Strings' --> to get the raw bytes/byte strings (b''), encode strings
    raw_bytes = next_lang.encode(encoding, errors=errors)

    # DBES - 'Decode Bytes, Encode Strings' --> to get the cooked strings, decode bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # printing the raw bytes, <===> printing the strings
    print(raw_bytes, '<===>', cooked_string)

# opening the Languages.txt using the UTF-8 encoding format and assigning it to a variable, languages
languages = open("Languages.txt", encoding="utf-8")

# calling the main() function with its necessary parameters (arguments)
main(languages, input_encoding, error)
