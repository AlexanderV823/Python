# Операции со строками
string = 'hello, world!'
print(string.upper()) #  Верхний регистр
print(string.lower()) #  Нижний регистр
print(string.capitalize()) #  Первая заглавная
new_string = string.replace('world', 'sanek').title() #  Замена все первые буквы заглавные
print(new_string) #  Вывод новой строки
print(string) #  Методы не изменяют исходную строку
string = string.upper() #  Перезаписываем исходную строку
print(string)
print(len(string)) #  Длина строки

# Строка относится к неизменяемому типу данных!
# Методы замены для строк, возвращают новые строки
# Код ниже вернет ошибку:
my_string = 'Sanek'
# my_string[0] = 's' # Вернет ошибку, т.к. строка не изменяемый тип
print(my_string)

name = 'sanek'
city = 'MOSCOW'
my_string = f'Hello, my name is {name.title()}, i live in {city.title()}'
print(my_string) #  при добавлении префикса 'f' можно встраивать в строку произвольные переменные 
print('Hello, my name is', name.title(), ', i live in', city.title()) #  Тот же вывод без 'f'

# Индексация и срезы строк
# Индексация начинается с 0 как и в 1С
my_string = 'Sanek'
print(my_string[1]) #  Прямой индекс
print(my_string[-4]) #  Обратный индекс
print(my_string[1:4]) # Левая граница включается, а правая нет!
print(my_string[1:4:2]) #  Шаг
print(my_string[1:]) #  Аналог Лев()
print(my_string[:4]) # Аналог Прав()
print(my_string[::-1]) # Выводит строку в обратном порядке

# Списки
# Похоже на Массив в 1С
list_0 = [] # Пустой список
user_list = ['Ваня', 'Петя', 'Ира']
table = [[1, 2, 3, 4], [5, 6, 78]] # Список может хранить списки
# Для списков существует множество операций, по аналогии как и в 1С
print(table[1][2]) # Получим 7

table_2 = user_list + table #  Так просто можно соединить списки
print(table_2)

del(user_list[-1]) #  Удаляем
print(user_list)

user_list.remove('Петя')  # Заменяем по значению
print(user_list)

user_list.append('Петя')  # Добавляем обратно (в конец)
print(user_list)

user_list.insert(1, 'Ира')  # Добавляем по индексу
print(user_list)

user_list.reverse()  # Инверсия
print(user_list)

# Список изменяемый тип данных
print(sorted(user_list, reverse=True)) #  Сортировка по убыванию
print(sorted(user_list)) #  Сортировка по возрастанию (по умолчанию)
print(user_list) # Функция sorted не изменила исходный список
user_list.sort() # Данный метод изменит исходные данные
print(user_list)
print(user_list.sort()) # Ничего не выведет, т.к. метод ничего нового не создает, а только меняет старое

string = 'Овен (21 марта – 19 апреля), Телец (20 апреля – 20 мая), Близнецы (21 мая – 20 июня), Рак (21 июня – 22 июля), Лев (23 июля – 22 августа), Дева (23 августа – 22 сентября), Весы (23 сентября – 22 октября), Скорпион (23 октября – 21 ноября), Стрелец (22 ноября – 21 декабря), Козерог (22 декабря – 19 января), Водолей (20 января – 18 февраля), Рыбы (19 февраля – 20 марта)'
print(string.split(',')) #  Разделение строки по запятой. Возвращает Список
list_1 = string.split(',')
print(','.join(list_1)) #  Объединяем список по заданному разделителю в Строку
# '\t' - табуляция
# '\n' - разрыв строки

#  Кортежи
#  Кортеж потребляет меньше памяти, чем Список
user_list = ('Ваня', 'Петя', 'Ира') #  Кортеж задается круглыми скобками
# user_list[0] = 'Гоша'  #  Тоже самое, что и Список, но Кортеж не изменяем. Вернет ошибку

my_list = list(user_list) #  Преобразуем Кортеж в Список
print(type(my_list))
my_list = tuple(my_list) #  Преобразуем Список в Кортеж
print(type(my_list))

# Функция ZIP
user_list = ('Ваня', 'Петя', 'Ира') #  Кортеж пользователей
salary_list = [100, 200, 50] # Список зарплат
salary_by_user = zip(user_list, salary_list) 
print(tuple(salary_by_user)) # Получим объединение по порядку значений

user_list = ('Ваня', 'Петя', 'Ира', 'Гоша') #  Кортеж пользователей
salary_list = [100, 200, 50] # Список зарплат
salary_by_user = zip(user_list, salary_list) 
print(tuple(salary_by_user)) #  Если для какого-то элемента нет пары, он не войдет в объединени

user_1, user_2, user_3, user_4 = user_list # Можно сразу записать в переменные по порядку через запятую.
print(len(user_list)) #  Главное совпадение количества перменных и элементов. Можно проверить через len
print(user_1, user_2, user_3, user_4)

# IN и NOT IN
# Проверка на вхождение
print('Ваня' in user_list) # Вернет Истину
print('Гиви' in user_list) # Вернет 
print('Ваня' not in user_list) # Вернет Ложь
print('Гиви' not in user_list) # Вернет Истину

# Циклы
x = 0
while x <= len(user_list): # Очень похоже на Пока ... Цикл в 1С
    print(f'В списке user_list есть значение с индексом: {x}')
    x += 1 # Эквивалент  x = x + 1, есть еще '-='

for user in user_list: # Аналог Для каждого .. из ... Цикл 1С
    print(user, end=';') #  Выведем через ;

salary_by_user = [['Ваня', 100], ['Петя', 200], ['Ира', 50], ['Гоша', 20], ['Вася', 300]]
print('\n')
for user in salary_by_user:
    print(f'Зарплата {user[0]} составляет {user[1]} рублей')

print('\n')
for user, salary in salary_by_user: #  Можно сразу достать в переменные
    if user == 'Ира':
        print('pass')
        pass # Аналог Возврат     
    elif user == 'Петя':
        print('continue')
        continue # Аналог Продолжить (переход в начало цикла)
    elif salary == 20:
       print('break')
       break # Аналог Прервать 
    else:
        print(f'Зарплата {user} составляет {salary} рублей')
    print(f'{user}: {salary}') #  Отступ имеет значение. В Python нет КонецЕсли и КонецЦикла
print(f'{salary_by_user}') #  Отступ имеет значение. В Python нет КонецЦикла