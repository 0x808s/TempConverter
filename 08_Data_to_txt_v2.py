data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

filename = input("Enter a filename (No extension please): ")

filename = filename + ".txt"


f = open(filename, "w+")

for item in data:
    f.write(item + "\n")

f.close()