elements = [(0,1,2,3,4,5,6,7,8,2), (1,2,2,2,3), 2, (2,2)]	# Make a list that contains lists

counter = 0	# We're going to count how many times 2 shows up

for i in elements:			# For each item in the list
	try:					# Try to iterate through it.
		for each in i:
			if each == 2:
				counter += 1# Increment when we find 2's.
	except:					# If we can't iterate though an item
		if i == 2:			# check if the item is a 2
			counter += 1	# increment if true.
print("The number of 2's is", counter)


print 'The length of each item is:'
for i in elements:		# For each item
	try:				# Try to print its length
		print len(i),
	except:				# If it doesn't have a length, assume it's length 1
		print 1,		# and not a list.