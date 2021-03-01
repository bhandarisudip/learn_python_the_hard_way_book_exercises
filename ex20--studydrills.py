#from package sys, import module argv
from sys import argv

#assign two parameters: script and input_file to a variable argv
script, input_file = argv

#define a function print_all, which takes f as an parameter
def print_all(f):
#first read the parameter f, then print it
	print(f.read())
	
#define a function called rewind, which takes f as a parameters	
def rewind(f): 
#Set the parameter's current position, using seek method, to 0
	f.seek(0)

#define print_a_line function that takes two parameters, line_count and f
def print_a_line(line_count, f): 
	print("line count=", line_count, "current line=", current_line)
#print the line count, and then read one entire line from the file using "readline"
	print(line_count, f.readline())

#open the input_file and assign it to the variable current_file
current_file = open(input_file)

#print "First, let's print the whole file", then create a new line
print("First, let's print the whole file:\n")

#call the function print_all, and assign the argument current_file to that function
print_all(current_file)

#print "Now let's rewind, kind of like a tape"
print("Now let's rewind, kind of like a tape.")

#call the function rewind and then assign current_file as its argument
rewind(current_file)

#print "Let's print three lines"
print("Let's print three lines:")

#create a variable called current_line and assign it a value of 1
current_line = 1
#call print_a_line function and assign it two arguments: current_line and current_file
print_a_line(current_line, current_file)

#add value '1' to the current_line
current_line += 1
#call the function print_a_line, and give it two arguments: current_line and current_file
print_a_line(current_line, current_file)

#add value '1' to the current_line again
current_line = current_line += 1
#call the function print_a_line, and give it two arguments: current_line and current_file
print_a_line(current_line, current_file)