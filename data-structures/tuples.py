first = (0, 1, 2)
second = (0, [1, 2])

try:
    first.append(3)
except AttributeError:
    pass

try:
    third = {first: 1}
    print(third)
except TypeError:
    print("First is un-hashable.")

try:
    fourth = {second: 2}
    print(fourth)
except TypeError:
    print("Second is un-hashble.")
