animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def printAnimal(index): 
	if index == 1: 
		num2en = "1st"
	elif index == 2: 
		num2en = "2nd"
	elif index == 3: 
		num2en = "3rd"
	else: 
		num2en = str(index) + "th"
	print(f"The {num2en} animal is at {index-1} and is a {animals[index-1]}")
	print(f"The animal at {index-1} is the {num2en} animal and is a {animals[index-1]}")

for i in range(1, 7):
	printAnimal(i)