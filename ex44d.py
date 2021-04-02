#create a Parent class
class Parent: 
	
	#create a method override that takes self as a parameter
	def override(self): 
	#print 'PARENT override()'
		print('PARENT override()')
	
	#create a method called implicit that takes self as a parameter
	def implicit(self): 
		#print 'PARENT override()''
		print('PARENT override()')
		
	#create a method called altered that takes self as a parameter	
	def altered(self): 
		#print 'PARENT altered()'
		print('PARENT altered()')

#create a Child class that inherits from Parent
class Child(Parent): 
	
	#create a method called override that takes self as a parameter
	def override(self): 
		#print 'CHILD override()'. This basically overrides the override method in Parent class.
		print('CHILD override()')
	
	#create a method called altered that takes self as a parameter
	def altered(self): 
		#print 'CHILD, BEFORE PARENT altered()'
		print('CHILD, BEFORE PARENT altered()')
		#call super with arguments Child and self, then call the function altered on whatever it returns
		super(Child, self).altered()
		#print 'CHILD, AFTER PARENT altered()'
		print('CHILD, AFTER PARENET altered()')

#assign Parent() class to a variable called dad
dad = Parent()
#assign Child() class to a variable called son
son = Child()

#call the method implicit from the variable dad
dad.implicit()
#call the method implicit from the variable son
son.implict()

#call the override method from the variable dad
dad.override()
#call the override method from the variable son
son.override()

#call the altered method from the variable dad
dad.altered()
#call the altered method from the variable son
son.altered()
