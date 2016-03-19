from __future__ import print_function
from time import sleep

def q_print(text):
	for i in text:
		print(i, end='')
		sleep(0.01)
	print("")

def room_start(map_vars = {'locked': True, 'spin': 0, 'buttons': [0, 0, 0]}):
	if map_vars['locked'] == True:
	# Locked state
		q_print("\nYou are in a dimly lit room. To the north is a large stone door with a bas-relief depicting four phases of the moon. \nThe stone door is too massive to move by hand.")
		q_print("To the south is an open passage, leading to another room.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go north")
		q_print("2. Go south")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "north" in choice or "North" in choice or choice == "n" or choice == "N":
			q_print("The stone door blocks your way...")
			raw_input()
			room_start(map_vars)
			
		elif "2" in choice or "south" in choice or "South" in choice or choice == "s" or choice == "S":
			q_print("You head south...")
			raw_input()
			room_spins(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			room_start(map_vars)
			
	else:
	# Unlocked state
		q_print("\nYou are in a dimly lit room. To the north is an open passage where the stone door used to be.")
		q_print("To the south is an open passage, leading to another room.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go north")
		q_print("2. Go south")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "north" in choice or "North" in choice or choice == "n" or choice == "N":
			q_print("You head north...")
			raw_input()
			room_goal(map_vars)
			
		elif "2" in choice or "south" in choice or "South" in choice or choice == "s" or choice == "S":
			q_print("You head south...")
			raw_input()
			room_spins(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			room_start(map_vars)

		
def room_goal(map_vars):
	q_print("You see daylight pouring through an exit. You can finally leave this place.")
	raw_input("\nThe End")
	exit(0)
	room_spins(map_vars)
	
def room_spins(map_vars):
	q_print("\nYou've entered a large, circular room. The walls are decorated with carvings of constellations from the night sky.")
	spin_funct(map_vars)
	
def spin_funct(map_vars):
	if map_vars['spin'] == 0:
	# North state
		q_print("The only exit is to the north.")
		q_print("There is pedestal in the center of the room. On it rests a globe carved of marble.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go north")
		q_print("2. Touch the globe")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "north" in choice or "North" in choice or choice == "n" or choice == "N":
			q_print("You head north...")
			raw_input()
			room_start(map_vars)
			
		elif "2" in choice or "touch" in choice or "Touch" in choice or "globe" in choice or "Globe" in choice:
			map_vars['spin'] = spin_it(map_vars['spin'])
			q_print("The globe gives way slightly when you touch it.")
			q_print("\nThe floor starts to shake and you hear a low grinding sound as the walls begin to rotate around you.")
			q_print("You look around, once everything has stopped moving.")
			raw_input()
			spin_funct(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			spin_funct(map_vars)
			
			
	if map_vars['spin'] == 1:
	# East state
		q_print("The only exit is to the east.")
		q_print("There is pedestal in the center of the room. On it rests a globe carved of marble.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go east")
		q_print("2. Touch the globe")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "east" in choice or "East" in choice or choice == "e" or choice == "E":
			q_print("You head east...")
			raw_input()
			room_east(map_vars)
			
		elif "2" in choice or "touch" in choice or "Touch" in choice or "globe" in choice or "Globe" in choice:
			map_vars['spin'] = spin_it(map_vars['spin'])
			q_print("The globe gives way slightly when you touch it.")
			q_print("\nThe floor starts to shake and you hear a low grinding sound as the walls begin to rotate around you.")
			q_print("You look around, once everything has stopped moving.")
			raw_input()
			spin_funct(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			spin_funct(map_vars)
	
	if map_vars['spin'] == 2:
	# South state
		q_print("The only exit is to the south.")
		q_print("There is pedestal in the center of the room. On it rests a globe carved of marble.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go south")
		q_print("2. Touch the globe")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "south" in choice or "South" in choice or choice == "e" or choice == "E":
			q_print("You head south...")
			raw_input()
			room_south(map_vars)
			
		elif "2" in choice or "touch" in choice or "Touch" in choice or "globe" in choice or "Globe" in choice:
			map_vars['spin'] = spin_it(map_vars['spin'])
			q_print("The globe gives way slightly when you touch it.")
			q_print("\nThe floor starts to shake and you hear a low grinding sound as the walls begin to rotate around you.")
			q_print("You look around, once everything has stopped moving.")
			raw_input()
			spin_funct(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			spin_funct(map_vars)
			
	if map_vars['spin'] == 3:
	# West state
		q_print("The only exit is to the west.")
		q_print("There is pedestal in the center of the room. On it rests a globe carved of marble.")
		raw_input()
		q_print("What will you do?")
		q_print("1. Go west")
		q_print("2. Touch the globe")
		
		choice = str(raw_input("> "))
		
		if "1" in choice or "west" in choice or "West" in choice or choice == "e" or choice == "E":
			q_print("You head west...")
			raw_input()
			room_west(map_vars)
			
		elif "2" in choice or "touch" in choice or "Touch" in choice or "globe" in choice or "Globe" in choice:
			map_vars['spin'] = spin_it(map_vars['spin'])
			q_print("The globe gives way slightly when you touch it.")
			q_print("\nThe floor starts to shake and you hear a low grinding sound as the walls begin to rotate around you.")
			q_print("You look around, once everything has stopped moving.")
			raw_input()
			spin_funct(map_vars)
			
		else:
			q_print("Nothing happens...")
			raw_input()
			spin_funct(map_vars)
			
			
	
def room_east(map_vars):
	# east room is button 0
	q_print("You are in a low vaulted room, little more than an alcove. \nBefore you is a detailed carving of the phases of the moon, surrounding what looks like a button.")
	q_print("The only exit is west, back the way you came.")
	
	raw_input()
	
	q_print("What will you do?")
	q_print("1. Go west")
	q_print("2. Press the button")
	
	choice = str(raw_input("> "))
	
	if "1" in choice or "west" in choice or "West" in choice or choice == "w" or choice == "W":
		q_print("You head west...")
		raw_input()
		room_spins(map_vars)
	
	elif "2" in choice or "button" in choice or "Button" in choice or "press" in choice or "Press" in choice:
		if map_vars['buttons'][0] == 0:
			q_print("The button pops down with a soft click.")
		else:
			q_print("The button pops up with a soft click.")
		
		map_vars['buttons'][0] = press(map_vars['buttons'][0])					# Toggle the button state
		if map_vars['buttons'] != [1, 1, 1] and map_vars['locked'] == False:	# Check if the door should be locked
			map_vars['locked'] = True
			q_print("You hear a loud rumbling, off in the distance.")
			
		if map_vars['buttons'] == [1, 1, 1]:					# Check if the door should be unlocked
			map_vars['locked'] = False
			q_print("You hear a loud rumbling, off in the distance.")
			
		raw_input()
		room_east(map_vars)
	
	else:
		q_print("Nothing happens...")
		raw_input()
		room_east(map_vars)

	
def room_south(map_vars):
	# south room is button 1
	q_print("You are in a low vaulted room, little more than an alcove. \nBefore you is a detailed carving of the phases of the moon, surrounding what looks like a button.")
	q_print("The only exit is north, back the way you came.")
	
	raw_input()
	
	q_print("What will you do?")
	q_print("1. Go north")
	q_print("2. Press the button")
	
	choice = str(raw_input("> "))
	
	if "1" in choice or "north" in choice or "North" in choice or choice == "n" or choice == "N":
		q_print("You head north...")
		raw_input()
		room_spins(map_vars)
	
	elif "2" in choice or "button" in choice or "Button" in choice or "press" in choice or "Press" in choice:
		if map_vars['buttons'][1] == 0:
			q_print("The button pops down with a soft click.")
		else:
			q_print("The button pops up with a soft click.")
		
		map_vars['buttons'][1] = press(map_vars['buttons'][1])					# Toggle the button state
		if map_vars['buttons'] != [1, 1, 1] and map_vars['locked'] == False:	# Check if the door should be locked
			map_vars['locked'] = True
			q_print("You hear a loud rumbling, off in the distance.")
			
		if map_vars['buttons'] == [1, 1, 1]:					# Check if the door should be unlocked
			map_vars['locked'] = False
			q_print("You hear a loud rumbling, off in the distance.")
			
		raw_input()
		room_south(map_vars)
	
	else:
		q_print("Nothing happens...")
		raw_input()
		room_south(map_vars)
	
def room_west(map_vars):
	# west room is button 2
	q_print("You are in a low vaulted room, little more than an alcove. \nBefore you is a detailed carving of the phases of the moon, surrounding what looks like a button.")
	q_print("The only exit is east, back the way you came.")
	
	raw_input()
	
	q_print("What will you do?")
	q_print("1. Go east")
	q_print("2. Press the button")
	
	choice = str(raw_input("> "))
	
	if "1" in choice or "east" in choice or "East" in choice or choice == "e" or choice == "E":
		q_print("You head east...")
		raw_input()
		room_spins(map_vars)
	
	elif "2" in choice or "button" in choice or "Button" in choice or "press" in choice or "Press" in choice:
		if map_vars['buttons'][2] == 0:
			q_print("The button pops down with a soft click.")
		else:
			q_print("The button pops up with a soft click.")
		
		map_vars['buttons'][2] = press(map_vars['buttons'][2])					# Toggle the button state
		if map_vars['buttons'] != [1, 1, 1] and map_vars['locked'] == False:	# Check if the door should be locked
			map_vars['locked'] = True
			q_print("You hear a loud rumbling, off in the distance.")
			
		if map_vars['buttons'] == [1, 1, 1]:					# Check if the door should be unlocked
			map_vars['locked'] = False
			q_print("You hear a loud rumbling, off in the distance.")
			
		raw_input()
		room_west(map_vars)
	
	else:
		q_print("Nothing happens...")
		raw_input()
		room_west(map_vars)
	
def map(location):
	return

def press(a):	
	a += 1
	a %= 2
	return a
	
def spin_it(a):
	a += 1
	a %= 4
	return a
	
room_start()
