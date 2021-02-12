#ex06-study drills 

#assign a string to x that includes a formatting character, which is then replaced by 10
x = "There are %d types of people."%10

#create a variable, binary, and assign the string "binary" to it
binary = 'binary'

#assign a new variable a string "don't" to a variable 'do_not' 
do_not = "don't"

#create a string called y, replace the formatting characters with variables "binary" and 
# "do_not". Example of two strings inside a string.
y = "Those who know %s and those who %s."%(binary, do_not)

#print x, i.e., "There are 10 types of people"
print(x)

#print y, i.e., "There are those who know binary and those who don't"
print(y)

#print "I said: There are 10 types of people". 
#Example of an integer (10) within a string (x), within a string "I said:"
print('I said: %r'%x)

#print "I also said: Those who know binary and those who do not". 
#Example of two strings (binary and do_not) within a string (y) within a string "I also said:"
print("I also said: '%s'"%y)

#assign boolean False to a variable hilarious
hilarious = False

#assign a string "Isn't that joke so funny?!" to a variable, joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#assign a string "This is the left side of the string..." to variable w.
w = 'This is the left side of the string...'

#assign "a string with a right side" to a variable e
e = 'a string with a right side'

#print "This is the left side of the string...a string with a right side"
#example of concatenating two strings with an operator '+'
print(w+e)