from __future__ import print_function
from time import sleep

test = """You are in a dimly lit room. To the north is a large stone door with a bas-relief depicting four phases of the moon.
The stone door is too massive to move by hand.
To the south is an open passage, leading to another room.

What will you do?
1. Go north
2. Go south
"""

def q_print(text):
	for i in text:
		print(i, end='')
		sleep(0.02)
		
q_print(test)