class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])
						
twinkle = Song("Twinkle twinkle/nLittle star/nHow I wonder/nWhat you are".split("/n"))
# passing a string to the Song class treats each character as a line
	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

twinkle.sing_me_a_song()
