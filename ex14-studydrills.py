#Exercise 14: study drills

#exercise 14: Prompting and Printing

from sys import argv

script, user_name = argv
unprompt = ': '

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print('Do you like me %s?' %user_name) 
likes = input(unprompt)

print("Where do you live %s?" %user_name)
lives = input(unprompt)

print("What type of computer do you have?")
computer = input(unprompt)

print("What's the name of your cat?")
cat = input(unprompt)

print ('''
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer. Nice.
You also have a cat named %r.
''' %(likes, lives, computer, cat))