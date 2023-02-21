first = 'python'
second = "Python"
third = """A multi-line string with
Python in it."""
low = third.index("P")
high = third.index(" i")

print(first, second, third, sep="\n")
print(third[low:high])
print(second[::-1] == "".join(reversed(second)))
print(f"Okay {second}.")