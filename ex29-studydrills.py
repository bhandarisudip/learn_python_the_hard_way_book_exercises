cats = 20 
dog = 30 
people = 15 

if people < cats:
	print("Too many cats! The world is doomed!")

if people > cats:
	print("Not many cats! The world is saved!")
	
if people < dogs: 
	print("The world is drooled on!")

if people > dogs: 
	print("The world is dry!")

dogs += 5

if people >= dogs: 
	print("People are greater than or equal to dogs.")
	
if people <= dogs: 
	print("People are less than or equal to dogs.")
	
if people == dogs: 
	print("People are dogs")


dogs +=5

if (people<dogs) and (dogs<cats): 
	print('Dogs are less than cats, but still they rule the world.')

if (dogs == cats) and (cats == people): 
	print('There are equal number of cats, dogs, and people.')
