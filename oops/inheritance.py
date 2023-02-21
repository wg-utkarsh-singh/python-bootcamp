class Terran():
    def __init__(self) -> None:
        print("Hello Terran")


class Animal():
    def __init__(self) -> None:
        print("Hello Animal.")


class Dog(Terran, Animal):
    def __init__(self) -> None:
        Terran.__init__(self)
        Animal.__init__(self)
        print("Hello Dog.")

Dog()
