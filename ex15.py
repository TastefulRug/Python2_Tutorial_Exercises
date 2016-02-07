# Imports the arguments variable from the sys library
# argv is a list of the script name and any arguments passed when running it
from sys import argv
# Unpack the argv into two variables.
# We want the first argument to be a filename
script, filename = argv
# Open the named file and save its contents to a variable
txt = open(filename)
# Print the filename
print "Here's your file %r:" % filename
# Print the file's contents by running the read command/function/method on it
print txt.read()
# close the file
txt.close()

# Repeat the above process using a raw_input prompt to get the filename
# instead of a comand line argument.
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
# close the file
txt_again.close()