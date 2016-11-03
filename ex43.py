# Notes on Top Down:
# Write or draw about the problem.
# Extract key concepts from 1 and research them.
# Create a class hierarchy and object map for the concepts.
# Code the classes and a test to run them.
# Repeat and refine.
# ------------------------------------------------------------------------------
# Notes on Bottom Up
# Take a small piece of the problem; hack on some code and get it to run barely.
# Refine the code into something more formal with classes and automated tests.
# Extract the key concepts you're using and try to find research for them.
# Write a description of what's really going on.
# Go back and refine the code, possibly throwing it out and starting over.
# Repeat, moving on to some other piece of the problem.

from sys import exit
from random import randint

class Scene(object):
# This base class isn't really needed. It's just here for practice.
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)


class Engine(object):
	
	def __init__(self, scene_map):
		# Initialize engine with Map() object
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()	# Set the current scene to opening scene from Map()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		# be sure to print out the last scene
		current_scene.enter()
		
class Death(Scene):
	
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if you were smarter.",
		"Such a loser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		pass
		
class LaserWeaponAmory(Scene):
	
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an"
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Armory and about to pull a weapon to blast you."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw, you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "completely ruins his brand new costume his mother bought him, which"
			print "makes him flay into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'
			
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge your foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'
			
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print "You tell the one Gothon joke you know:"
			print "Lbhe zbugre vf fb sng, jura fur fvgf neghaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
			print "The Gothon stops, tries not to laugh, then bursts out laughing and can't move."
			print "While he's laughing you run up and shoot him square in the head"
			print "putting him down, then you jump through the Weapons Armory door."
			return 'laser_weapon_armory'
			
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor"
			
class TheBridge(Scene):
	
	def enter(self):
		pass
		
class EscapePod(Scene):
	
	def enter(self):
		pass
		
class Map(object):
	# Dictionary of scenes
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponAmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished(),
	}
	
	def __init__(self, start_scene):
		# starting scene will be the argv of Map()
		self.start_scene = start_scene
		
		
	def next_scene(self, scene_name):
		# Get a scene from the scene dict
		val = Map.scenes.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
		
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
