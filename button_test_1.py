# Experimenting with a button that cycles through states
button = 0
direction = ['north', 'east', 'south', 'west']

while True:
	print "The arrow is facing %s." % str(direction[button])

	raw_input("Press the button.\n")

	button += 1 # Increase button by one
	button %= 4 # Make sure button can have only 4 possible values: 0-3