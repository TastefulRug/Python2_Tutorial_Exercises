name = 'Zed A. Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# Newer string formatting?
print 'We are the {} who say "{}"'.format('knights', 'Ni')
# The brackets{} and characters within them (called format fields) are replaced with the objects 
# passed into the str.format() method. A number in the brackets {0} refers to the position of the 
# object passed into the str.format() method.

# Taken from https://docs.python.org/2/tutorial/inputoutput.html#fancier-output-formatting