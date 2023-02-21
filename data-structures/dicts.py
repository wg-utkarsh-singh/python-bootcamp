first = {"one": 1, "two": 2, "three": 3}
second = {(0, 1, 2): 3, (1, 2): 2, (2): 1}

print(first["three"] == second[(0, 1, 2)])
print(first.keys())
print(first.values())
print(first.items())
