class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

cat1 = Cat("Персидская", "Мурзик", 3)
cat2 = Cat("Сиамская", "Саймон", 5)
cat3 = Cat("Британская", "Барсик", 2)

print("Информация о котах:")
print("Кот 1:", cat1.breed, cat1.name, cat1.age)
print("Кот 2:", cat2.breed, cat2.name, cat2.age)
print("Кот 3:", cat3.breed, cat3.name, cat3.age)