
from collections import deque
calculations = deque()


for item in range(0, 5):
    get_item = input("Enter an item: ")

    calculations.appendleft(get_item)


print()
print("*** The Full List ***")
print(calculations)

print()

print("*** Most Recent 3 ***")
for item in range(0,3):
    print(calculations[item])