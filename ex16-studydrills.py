#A script similar to ex15 that uses read and argv to read the file 

from sys import argv

script, filename = argv

print("Here is the content of the file:")
txt = open(filename)
content = txt.read()
print(content)
txt.close()