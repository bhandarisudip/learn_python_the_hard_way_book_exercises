print("You enter a dark room with no doors. Do you go through door #1, door #2, or door #3?")

door = input("> ")

if door == "1": 
	print("There's a giant bear here eating a cheese cake. What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	
	bear = input("> ")
	
	if bear == "1": 
		print("The bear eats your face off. Good job!")
	elif bear == "2": 
		print("The bear eats your legs off. Good job!")
	else: 
		print(f"Well, doing {bear} is probably better. Bear runs away.")

elif door == "2": 
	print("You stare into the endless abyss at Cthulu's retina.") 
	print("1. Blueberries.") 
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
	
	insanity = input("> ") 
	
	if insanity == "1" or insanity == "2": 
		print("Your body survives powered by a mind of jello. Good job!") 
	else: 
		print("The insanity rots your eyes into a pool of muck. Good job!") 
		

elif door == '3': 
	print("You enter a new country.")
	print("1. Mexico")
	print("2. United States")
	print("3. Belgium")
	print("4. Japan")
	
	country = input("> ") 
	
	if country == '1' or country == '2': 
		print("You are in North America.") 
	elif country == '3': 
		print("You are in Europe.")
	else: 
		print("You are in Asia.")

else: 
	print("You stumble around and fall on a kinfe and die. Good job!")