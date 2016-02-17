# import argument variable
from sys import argv
# unpack arguments
script, input_file = argv
# function to read and print all of something
def print_all(f):
	print f.read()
# function to set the file pointer back to start of file	
def rewind(f):
	f.seek(0)
# function to print a specific line
def print_a_line(line_count, f):
	print line_count, f.readline(),# the comma prevents an extra \n character 
# the line_count variable doesn't actually tell the function which line to print
# it just prints its contents before the readline()
# readline() will just page through the file one line at a time without direction

# open the input file	
current_file = open(input_file)

print "First let's print the whole file:\n"
# print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# set file pointer to start of file
rewind(current_file)

print "Let's print three lines:"
# print the number 1, followed by a line from the file
current_line = 1
print_a_line(current_line, current_file)
# print the number 2 followed by a line
current_line += 1
print_a_line(current_line, current_file)
# print the number 3 followed by a line
current_line += 1
print_a_line(current_line, current_file)

# errors:
# mixed up current_file and current_line variable on line 35
# they have overly similar names
# Tried to increment a variable that didn't exist yet on line 31