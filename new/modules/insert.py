from sys import argv

script, filename = argv

target = open(filename, 'w')

text = raw_input("> ")

target.write(text)
