#ex11: Asking questions 

print('How old are you?', end=' ')
age = input()

print('How tall are you?', end=' ')
height = input()

print('How much do you weigh?', end=' ')
weight = input()

print("So, you're {} years old, {} tall, and {} heavy.".format(age, height, weight))


#ask some other questions: 
print('What is your name?', end=' ')
name = str(input())

print('Where do you live?', end=' ')
address = input()

print('Enter an integer:', end=' ')
num = int(input())

print("How many hours does {} play outside?".format(name), end=' ')
play_hrs = int(input())

print("What's the population of %s?"%address, end=' ')
population = int(input())

print("{} lives in {}. Population of {} is {}. {} is an integer. {} only plays outside for {} hours.".format(name,address,address,population,num,name,play_hrs))

print('If you add %d and %d you get %d'%(num, play_hrs, num+play_hrs))


