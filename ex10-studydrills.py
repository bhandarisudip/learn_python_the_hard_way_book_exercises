#Exercise 10--Study Drills

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#combine escape sequences and format strings to create a more complex format.
months = "I'll print the first six months in a year:"
jan = 'January'
feb = 'February'
mar = 'March'
apr = 'April'
may = 'May'
jun = 'June'

print('%s \n\t%s \n\t%s \n\t%s \n\t%s \n\t%s \n\t%s' %(months, jan, feb, mar, apr, may, jun))


print("%r" %months)
print("%r" % "He said \"I'll print the first six months in a year\"")

print("%s" %months)
print("%s" % "He said \"I'll print the first six months in a year\"")
