#ex5: More Variables and Printing

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches 
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." %name)
print("He's %d inches tall." %height)
print("He's %d pounds heavy." %weight)
print("Actualy that's not too heavy")
print ("He's got %s eyes and %s hair" %(eyes, hair))
print('His teeth are usually %s depending on the coffee.' %teeth)

# this line is tricky, try to get it exactly right
print ('If I add %d, %d, and %d, I get %d.' %(age, height, weight, age + height + weight))

# try more format characters
my_greeting = 'Hello'
my_first_name = 'Sudip'
my_last_name = 'Bhandari'
my_favorite_food = 'Momo'
my_age = 30
# print "Hello, my name is Sudip Bhandari. My favorite food is momo. I am 30 years old."
print('%s. My name is %s %s. My favorite food is %s. I am %d years old.'%(my_greeting, my_first_name, my_last_name, my_favorite_food, my_age))

# Try to write some variables that convert the inches and pounds to centimeters and kilos 
cm_per_inch = 2.54
kilo_per_pound = 0.45

print('Zed is %d centimeters tall'%(height*cm_per_inch))
print('He is %d kilos heavy'%(weight*kilo_per_pound))
