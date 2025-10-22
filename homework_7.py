class Animal():
    def __init__(self, name: str, weight: int, sound: str, food: str):
        self.name = name
        self.weight = weight
        self.sound = sound
        self.food = food

    def make_sound(self):
        print(self.sound)

    def eat(self):
        print(f'Это животное кушает: {self.food}')

class Bird(Animal):
    def __init__(self, name, weight, sound, food, egg):
        self.egg = egg
        super().__init__(name, weight, sound, food)

    def make_egg(self):
        print(f'средний вес яйца: {self.egg}')

class DairyAnimal(Animal): 
    def __init__(self, name, weight, sound, food):
        super().__init__(name, weight, sound, food)

class Goose(Bird):
    def __init__(self, name: str, weight: int, sound='Га-га-га', food='Трава', egg=40):
        super().__init__(name, weight, sound, food, egg)

class Cow(DairyAnimal):

    def __init__(self, name, weight, sound, food, sum_milk):
        self.sum_milk = sum_milk
        super().__init__(name, weight, sound, food)

    def make_milk(self):
        print(f'Корова {self.name} дает удоя {self.sum_milk} литров молока')


goose_1 = Goose('Серый', 7)
goose_2 = Goose('Белый', 8)
print(f'Имя первого гуся: {goose_1.name}. Вес второго: {goose_2.weight}')
goose_1.make_egg()
goose_2.make_sound()
goose_1.eat()

cow_1 = Cow('Зорька', 135, 'Муу-муу', 'Трава/сено', 5)
print(f'Корова {cow_1.name} весит {cow_1.weight} кушает {cow_1.food}')
cow_1.make_sound()
cow_1.make_milk()
cow_1.eat()