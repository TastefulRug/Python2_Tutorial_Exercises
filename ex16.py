from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')
# Mode arguments for Open
# r 	read
# w		write
# r+	read and write, pointer at start of file
# w+	read and write, overwrites the existing file if the file exists. 
# 		If the file does not exist, creates a new file for reading and writing.
# a 	Opens file for appending. Pointer is at end of file. Creates file if it doesn't exist
# a+	Opens for appending and reading. Pointer at end of file

print "Truncating the file. Goodbye!"
# target.truncate() #not needed because we opened it in a write mode

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write('%s\n%s\n%s\n' % (line1, line2, line3))

# target2 = open(filename, 'r') # Don't need to open second time to read

print "You wrote: "

target.seek(0, 0)
# Sets pointer back to begining of file
# Telling python to read a all of a txt file it's at the end of adds lots
# of white space and weird characters. Seek to start first.
print target.read()

print "And finally, we close it."
target.close()