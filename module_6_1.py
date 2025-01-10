class Animal:
    def __init__(self, name1):
        self.name1 = name1
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name1} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name1} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{self.name1} не может съесть {food.name}")


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    pass  # Здесь можно добавить другие методы или атрибуты, специфичные для млекопитающих


class Predator(Animal):
    pass  # Здесь можно добавить другие методы или атрибуты, специфичные для хищников


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name1)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
