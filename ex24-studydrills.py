print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation 
\n\t\t where there is none.
"""

print("-----------")
print(poem)
print("-----------")

five = 10-2+3-6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars/100
	return jelly_beans, jars, crates

start_point = 10000
#assign variables beans, jars, and crates from the returns of the function "secret_formula"
beans, jars, crates = secret_formula(start_point)

print(f"With a starting point of {start_point}.")
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")


start_point = start_point/10

print("We can also do that this way:")
#call the function and use its return values as the parameters for the formatters
print("We'd have %d beans, %d jars, and %d crates."%secret_formula(start_point))