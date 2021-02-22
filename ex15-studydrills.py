#Exercise 15 Study Drills

#import module argv from sys package
from sys import argv

#provide two arguments "script" and "filename" to argv
script, filename = argv

#open the file and assign it to a variable "txt"
txt = open(filename)

#print the name of the file after printing "Here's your file:"
print("Here's your file %r: " %filename)
#read the opened file that was assigned to the variable "txt", and then print it
print(txt.read())

#close the file
txt.close()

#print "Type your filename again" string
print("Type your filename again:")
#ask user for the input after printing ">", and assign the user input to variable file_again
file_again = input("> ")

#open the file_again variable
txt_again = open(file_again)

#read the file_again variable using ".read" method, and then print it.
print(txt_again.read())

#close the file
txt_again.close()