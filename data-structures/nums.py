from math import fsum

print(3 + 1)
print(0.1 + 0.2 == 0.3,
      round(0.1 + 0.2, 10) == round(0.3, 10),
      sep="\n")
print(0.3.hex())
print(sum([0.1] * 10))
print(fsum([0.1] * 10))