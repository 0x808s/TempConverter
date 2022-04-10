data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

filename = input("Enter a filename: ")

f = open(filename, "w+")

for item in data:
    f.write(item)

f.close()