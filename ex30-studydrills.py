#create a new variable called people and assign value 50 to it
people = 50 

#create a new variable cars and assign value 40 to it
cars = 40

#create a new variable buses and assign value 100 to it
buses = 100

#compare if value of cars is greater than the value assigned to people: 
if cars > people: 
	#Print "We should take the cars"
	print("We should take the cars.")
#compare value for cars with people
elif cars < people: 
	#print "We should not take the cars"
	print("We should not take the cars.")	
#create an else statement, i.e., if cars are equal to people
else: 
#print "We can't decide"
	print("We can't decide.")
	
#compare buses with cars, if value for buses are greater than cars
if buses > cars: 
#print "That's too many buses"
	print("That's too many buses.")
#compare if value for buses are less than cars
elif buses < cars: 
#print"May be we could take the buses.""
	print("May be we could take the buses.")
#create an else statement
else: 
#print "We still can't decide"
	print("We still can't decide.")
	
#compare value for people with buses
if people > buses: 
#print "Alright, let's just take the buses"
	print("Alright, let's just take the buses.")
#create an else statement, i.e., if people are less than cars and buses
else: 
#print "Fine, let's stay home then."
	print("Fine, let's stay home then.")