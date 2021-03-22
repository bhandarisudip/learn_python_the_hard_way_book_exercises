class Song(object): 
	
	def __init__(self, lyrics): 
		self.lyrics = lyrics
	
	def sing_me_a_song(self): 
		for line in self.lyrics: 
			print(line)

happy_bday = Song(["Happy birthday to you.", 
				   "I don't want to get sued", 
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", 
						"With pockets full of shells"])

knocking_on_heavens_door = Song(["Mama take my ** from the ground.", 
								 "I don't want to take it anymore.", 
								 "Knock, knock, knocking on heaven's door."])

when_we_were_young = Song(["You sit there in your heart ache.", 
						   "Waiting for a beautiful boy to.", 
						   "Save you from you old ways.", 
						   "You play forgiveness but watch it now here it comes."])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

knocking_on_heavens_door.sing_me_a_song()

when_we_were_young.sing_me_a_song()