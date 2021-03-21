#create a mapping of state to abbreviation 
states = {
		'Bagmati': 'BGM',
		'Narayani': 'NRY', 
		'Janakpur': 'JKP', 
		'Seti': 'SEI', 
		'Bheri': 'BER'
	}

#create a basic set of states and some cities in them
cities = {
		'BGM': 'Kathmandu', 
		'SEI': 'Dhangadi', 
		'BER': 'Doti'
	}
	
# add some more cities 
cities['NRY'] = 'Chitwan'
cities['JKP'] = 'Janakpurdham'

#print out some cities 
print('-' * 10)
print(f"BGM state has: cities['BGM']")
print("SEI state has: ", cities['SEI'])

#print some states 
print('–' * 10)
print(f"Narayani's abbreviation is {states['Narayani']}")
print(f"Bheri's abbreviation is {states['Bheri']})

# do it by using the state then cities dict
print('–' * 10)
print(f"Seti has {cities[states['Seti']]}")
print(f"Janakpur has {cities[states['Janakpur']]}")

# print every state abbreviation
print('–' * 10)
for state, abbrev in states.items():
	print(f"{state} is abbreviated {abbrev}")

# print every city in state 
print('-' * 10)
for abbrev, city in cities.items():
	print(f"{abbrev} has the city {cities[city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in states.items(): 
	print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")


print('–' * 10)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state: 
	print("Sorry, no Texas.")

#get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: {city}"