#creates a new function called cheese_and_crackers and takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#print "You have cheese_count cheeses" (replace cheese_count with the user input)
	print("You have %d cheeses!" %cheese_count)

	#print "You have cheese_count cheeses" (replace cheese_count with the user input)
	print("You have %d boxes of crackers!" %boxes_of_crackers)

	#print "Man that's enough for a party" string
	print("Man that's enough for a party")

	#print"Get a blanket and then create a new line after this string."
	print("Get a blanket. \n")
	
#print a string "We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
#take two arguments for the function cheese_and_crackers: 20, and 30
cheese_and_crackers(20,30)

#print "Or, we can use variables for our script:"
print("Or, we can use variables from our script:")
#assign 10 to a variable amount_of_cheese
amount_of_cheese = 10 
#assign 50 to a variable amount_of_crackers
amount_of_crackers = 50 

#assign the two arguments amount_of_cheese and amount_of_crackers to cheese_and_crackers function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#print "We can even do math inside too:"
print("We can even do math inside too:")
#assign 10+20 number and 5+6 number inside cheese_and_crackers function
cheese_and_crackers(10+20, 5+6)

#print "And we can combine the two, variables and math"
print("And we can combine the two, variables and math:")
#Assign two arguments to cheese_and_crackers function. One argument is amount_of_cheese 
	#variable+100 (where 100 is an integer), and another argument is amount_of_crackers+1000 
	#where 1000 is an integer
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)




def sum_two_arguments(a,b): 
	print(a+b)

#1. use numbers as parameters
sum_two_arguments(20,10)

#2. use strings as parameters
sum_two_arguments('red', 'blue')

#3. use variables as parameters
x = 5
y = 6

#4. use one variable as parameter, another parameters as number
sum_two_arguments(x, y)

#5. multiply a number with a variable as parameters
sum_two_arguments(x*10, y*20)

#6. multiply a number with a variable as one parameter, add two numbers as the second parameter
sum_two_arguments(x*10, y*20)

#7. add two numbers as parameters
sum_two_arguments(10+10, 20+20)

#8. divide one variable with another as parameters
sum_two_arguments(x/y, y/x)

#9. divide one variable with another as first parameter, divide another variable by a number as the 
	#second parameter
sum_two_arguments(x/y, y/5)

#10. do arithmetic for one parameter, include a number (1) as another parameter
sum_two_arguments(x*10/y, 1)