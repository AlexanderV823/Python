# Словари

tel_dict = dict() # Задается функцией
city_dict = {'А': ('Архангельск', 'Астрахань'), 'М': ('Москва', 'Мурманск')} # Или фигурными скобками
print(city_dict)
city_dict['С'] = ('Сыктывкар', 'Салехард') # Добавление нового элемента. Обращение только по ключу
city_dict.setdefault('К', ('Кострома', 'Калининград'))
print(city_dict)

for letter, city_tuple in city_dict.items():
    print(f'Города на букву {letter.upper()}:')
    for city in city_tuple:
        print(f'{city}')
    print()

print(city_dict.keys()) # Важная функция для проверки ключей
# В целом над словарями доступен стандартный набор операций

# Множества
# Содержат неповторяющиеся элементы в СЛУЧАЙНОМ порядке!. Не позволяет записать дубли

city = set() # Инициируется функцией set()
country = set()

# Операции над множествами
city_and_country = city | country # Объединение. Логическое ИЛИ
city_and_country = city & country # Пересечение. Логическое И
city_and_country = city - country # Разность. Выведет только города
city_and_country = city ^ country # Симметричная разность. Выведет не пересекающиеся города и страны
# Набор операций стандартен
country.difference(city) # Вернет Страны, не принадлежащие множеству Города
country.symmetric_difference(city) # Вернет Страны, которые не встречаются в множестве Страны и Города
alphabet = frozenset() # "Замороженное" неизменяемое множество

# enumerate()

for id, letter in enumerate(city_dict):
    print(f'Позиция словаря: {id}, Буква: {letter}')
print(f'Функция enumerate() возвращает в первую переменную номер текущей обрабатываемой позиции')