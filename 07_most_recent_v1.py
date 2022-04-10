all_calculations = []

for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

all_calculations.reverse()

print()
print("***THE FULL LIST***")
for item in all_calculations:
    print(item)

print()

print("***MOST RECENT 3 ***")
for item in range(0, 3):
    print(all_calculations[item])
