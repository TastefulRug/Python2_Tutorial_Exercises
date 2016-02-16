# This one is like your script with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	# python ignores the white space after the comma in parenthesises
	# use whatever is more readable
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
	print "I got nothin'."
	
	
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
# lesson ends here

# seeing if I can stick functions inside of functions
def print_all(arg1, arg2, arg3):
	print_two_again(arg1, arg2)
	print_one(arg3)
	print_none()

print_all("one", "two", 'three')
# turns out I can