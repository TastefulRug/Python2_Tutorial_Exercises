from decimal import *	# So I dont have to deal with floating point numbers
getcontext().prec = 3	# Set the precision of decimals

# Note: Decimal() has to be capitalized for some reason

i = abs(Decimal(raw_input("Range start? "))) # Input has to be converted to a number
end = abs(Decimal(raw_input("Range end? ")))
step = abs(Decimal(raw_input("Increment by? ")))
# Use abs() to avoid negative numbers and infinite loops

if step == 0: # Infite loops are bad
	step = 1

numbers = []

def linear_list(i, end, step):
	"""This function takes a range and increment value and uses those to generate a 
	list, while telling you way too much about what it's doing.
	linear_list( range_start, range_end, increment_value )"""
	while i < end:
		print "\nAt the top i is %s" % i
		numbers.append(i)
	
		i += step
		print "Numbers now: ",
		for num in numbers:
			print "%s," % num,	# This line gets nice looking commas in the list
		print "\nAt the bottom i is %s" % i

linear_list(i, end, step)

print "The numbers: "

for num in numbers:
	print num