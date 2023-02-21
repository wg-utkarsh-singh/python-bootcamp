def hello_world():
    print(f"Hello World")


def hello_name(name):
    print(f"Hello {name}")


def hello_bool(boolean):
    if boolean:
        return "Hello"
    return "Goodbye"


def cond_bool(a, b, c):
    if c:
        return a
    return b


def sum_2(a, b):
    return a + b


def is_even(num):
    return num % 2 == 0


def is_greater(a, b):
    if a > b:
        return True
    return False


def sum_any(*arg):
    return sum(arg)


def filter_even(*arg):
    return [x for x in arg if x % 2 == 0]


def skyline(string):
    rslt = ""
    for idx, ch in enumerate(string):
        if idx % 2 == 0:
            rslt += ch.upper()
        else:
            rslt += ch.lower()
    return rslt
