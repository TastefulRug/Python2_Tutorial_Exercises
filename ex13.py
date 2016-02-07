from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

var1 = raw_input(script+"? ")
# Adding a space inside the raw_input() prompt required
# a + sign, ie. string addition. A comma didn't work
print "You typed %r." % var1