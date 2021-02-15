#exercise 7--study drills 

#prints a string: 'Mary had a little lamb.'
print("Mary had a little lamb.")

#prints a string: 'Its fleece was white as snow.'
print("Its fleece was white as %s." %'snow')

#prints a string: 'And everything that Mary went.'
print("And everything that Mary went.")

#prints "." ten times
print("." * 10) #what'd that do? -- '*' operator for strings used to repeat a character for certain times

#assign a string character 'C' to variable end1
end1 = "C"

#assign a string character 'h' to variable end2
end2 = "h"

#assign a string character 'e' to variable end3
end3 = "e"

#assign a string character 'e' to variable end4
end4 = "e"

#assign a string character 's' to variable end5
end5 = "s"

#assign a string character 'e' to variable end6
end6 = "e"

#assign a string 'B' to variable end7
end7 = "B"

#assign a string 'u' to variable end8
end8 = "u"

#assign a string 'r' to variable end9
end9 = "r"

#assign a string 'g' to variable end10
end10 = "g"

#assign a string 'e' to variable end11
end11 = "e"

#assign a string 'r' to variable end12
end12 = "r"

#print a concatenation of strings end1 through end6, create a space using a comma ',' 
#then print a concatenation of strings end7 through end12 in the same line.
print(end1+end2+end3+end4+end5+end6, end7+end8+end9+end10+end11+end12)

#this also prints 'Cheese Burger' but instead of concatenating all the variables in one 
#line, it concatenates the end1-end6, then using a statement end = ' ' concatenates 
#the remaining variables end7-end12 from another line
print(end1+end2+end3+end4+end5+end6, end = " ") 
print(end7+end8+end9+end10+end11+end12)