def add (a, b): 
	print("Adding %d + %d" %(a,b))
	return a+b 

def subtract (a, b): 
	print("Subtracting %d - %d" %(a,b))
	return a - b

def multiply (a, b): 
	print("Multiplying %d * %d" % (a, b))
	return a*b

def divide(a, b): 
	print("Dividing %d / %d" %(a,b))
	return a/b
	
#a new function to test return
def isequal(a, b): 
	print(f"Is {a} equal to {b}? ",end="")
	return a==b


print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))

#A puzzle for the extra credit, type it in anyway. 

print("Here is a puzzle.")

what = add(age, multiply(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

#test the return value of isequal
num1 = 40 
num2 = 50
num3 = 50 

print(isequal(num1, num2))
print(isequal(num2, num3))


#write a simple formula and use the function again 
a = 10 
b = 20 
c = 30 
d = 40 

e = (multiply(divide(d,subtract(a,add(b,c))), 2))
print(f"The final number is {e}.")

