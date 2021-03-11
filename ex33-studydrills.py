numbers = []

def while_loop(x, increment): 
	while i<x: 
		print(f"At the top i is {i}")
		numbers.append(i)
	
		i = i+increment
		print("Numbers now: ", numbers)
	
		print(f"At the bottom i is {i}")
	
print('The numbers: ')

for num in numbers:
	print(num)
	
	
numbers = []

def while_loop(x, increment): 
	for i in range(0,x,increment):
		print(f"At the top i is {i}")
		numbers.append(i)
	
# 		i = i+increment
		print("Numbers now: ", numbers)
	
		print(f"At the bottom i is {i}")
	
print('The numbers: ')

for num in numbers:
	print(num)