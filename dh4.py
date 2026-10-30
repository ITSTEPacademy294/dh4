
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "їсть")

    def sleep(self):
        print(self.name, "спить")


class Dog(Animal):
    def bark(self):
        print(self.name, "гавкає: Гав-гав!")


class Cat(Animal):
    def meow(self):
        print(self.name, "нявкає: Няв!")


dog = Dog("Боня", 3)
cat = Cat("Марко", 10)

print("--- Собака ---")
print("Ім'я:", dog.name)
print("Вік:", dog.age)
dog.eat()
dog.sleep()
dog.bark()

print("\n--- Кіт ---")
print("Ім'я:", cat.name)
print("Вік:", cat.age)
cat.eat()
cat.sleep()
cat.meow()
