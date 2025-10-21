# Инкапсуляция

class UserPerson:
    name = str()
    department = str()
    salary = int()

class UserPerson:
    lead = UserPerson()

    def _change_salary(self, sum: int): # Одинарное _ перед говорит о том, что этот атрибут или метод лучше не использовать вне класса, но он извне остается доступен
        self.salary += sum

class Department:
    def __init__(self, name='Отдел 1'): # В атрибутах указываются обязательные значения
        self.name = name
        self.lead = UserPerson()
        self.__users = [] # Двойное __ позволяет защитить метод или атрибут от использования из вне

ITDep = Department('ИТ отдел')

# print(ITDep.__users) # Выдаст ошибку
ITDep._Department__users = ['Иванов', 'Петров'] # При этом двойное подчеркивание можно легко обойти таким образом
print(ITDep._Department__users)

class Lead(UserPerson): # В скобках указывается класс, чьи атрибуты унаследует текущий класс
    
    def __init__(self):
        super().__init__()
        
    def _SendTask(self, task, worker): # При этом добавляем новому классу метод, который будет свойственен только ему
        self.task = task
        self.worker = worker

# Наследование

class Worker():
    def __init__(self, name, salary=100):
        self.name = name
        self.salary = salary

    def work(self):
        self.salary += 100 

class Lead():
    
    def __init__(self, worker):
        self.slave = worker # При этом добавляем новому классу атрибут, который будет свойственен только ему
        
    def SendTask(self, task, worker):
        self.task = task
        self.worker = worker

print(Lead.mro())

class Ceo(Worker, Lead): #Можно объединять наследование, приоритет наследования, согласно порядку в скобках
    def __init__(self, name, workers=100):
        self.workers = workers
        super().__init__(name, salary=1000)
    
    def _kick_out(self, worker):
        super().worker = worker

    def work(self):
        super().work()
        super().SendTask()

# Полиморфизм
# Задание логики сравнения классов

    def __lt__(self, other):
        if isinstance(other, Ceo):
            return self.workers < other.workers # Переделать на сравнение 
        else:
            print('Не CEO')  

print(Ceo.mro())

ceo_1 = Ceo('Иванов', 200)
ceo_2 = Ceo('Петров', 300)

print(ceo_1 < ceo_2) # Вернет Истину
print(ceo_1.name)
print(ceo_1.workers)
print(ceo_1.salary)

worker = Worker('Сидоров')

print(ceo_1 < worker) # Вернет 'Не CEO' и None