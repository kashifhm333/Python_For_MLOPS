class football:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

ronaldo = football("Cristiano Ronaldo", 38)
ronaldo.display()
messi = football("Lionel Messi", 36)
messi.display()