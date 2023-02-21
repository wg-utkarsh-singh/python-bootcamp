with open("test.txt", "r+") as f:
    print(f.read())
    f.write("Third Line\n")
    f.seek(0)
    print(f.read())