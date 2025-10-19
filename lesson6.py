# Объекты и классы

# Задание атрибутов класса:
class UserPerson: # Классы именуются с заглавных букв без разделителей (как все в 1С)
    name = str()
    department = str()
    # lead = UserPerson() # Сразу же сослаться на создаваемый класс нельзя
    salary = int()

class UserPerson:
    lead = UserPerson()
# Задание методов класса:
    def change_salary(self, sum: int): # Первый параметр self - объект класса, который будет передаваться в функцию
        self.salary += sum

class Department:
    def __init__(self, name='Отдел 1'): # В атрибутах указываются обязательные значения
        self.name = name
        self.lead = UserPerson()
        self.users = [] # Если так указать, то у каждого объекта класса будет свой список

user_1 = UserPerson()
user_1.name = 'Петя'
user_1.department = 'ИТ-отдел'
user_1.salary = 1000

user_2 = UserPerson()
user_2.name = 'Вася'
user_2.department = 'ИТ-отдел'
user_2.lead = user_1
user_2.salary = 800

print(user_1.__dict__) # Выведет все добавленное в объект класса
print(user_2.__dict__)

user_2.change_salary(200)
print(user_2.__dict__)

new_dep = Department()
print(new_dep.__dict__)

print(isinstance(new_dep, UserPerson)) # Проверка на соответвтие классу. Вернет Ложь