from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Seeing if input matches a variable
var1 = raw_input("What is the name of this script? ")
if var1 == script:
	print "Correct!"
# Did this to figure out how Python does if statements
else:
	print "Wrong! It's %s." % script
# Printing the argument variable
print argv

string = 'Hellow World'
# For each character in the string, print that character
for x in string:
	print x