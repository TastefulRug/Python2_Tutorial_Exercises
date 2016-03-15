# Experiementing with a simple button that toggles on/off

button = False
light = ['bright', 'dark']

while True:
	# if button == True: print "Hey, it's too bright in here."
	# else: print "Hey, it's too dark in here."
	print "Hey, it's too %s in here." % str(light[button])
	raw_input("Flick the light switch? ")
	print "\nClick!\n"
	button = not button