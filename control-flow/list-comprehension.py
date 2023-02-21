print([x * x for x in range(5)])
print([x * x for x in range(10) if x % 2 == 0])
print([(x, "EVEN") if x % 2 == 0 else (x, "ODD") for x in range(5)])
print([(x, y) for x in range(2) for y in range(5)])
