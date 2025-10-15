# Задача 1

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
only_russia_geo_logs = []

for visit_dict in geo_logs:
    for visit_id, locations in visit_dict.items():
        for location in locations:
            if location == 'Россия':
                only_russia_geo_logs.append({visit_id: locations})
print(only_russia_geo_logs)

# Задача 2

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

unic_ids = set()

for user_id, list  in  ids.items():
    unic_ids.update(list)
print(unic_ids)

# Задача 3

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'курc',
    'сериалы про спорт'
    ]

total_queries = len(queries)
queries_dict = dict()

for string in queries:
    if queries_dict.get(len(string.split())) is None:
        queries_dict[len(string.split())] = 1
    else:
        x = queries_dict.get(len(string.split()))
        queries_dict[len(string.split())] = x + 1                      

print(total_queries, queries_dict)

for key, value in queries_dict.items():
    print(f'Поисковых запросов содержащих {key} слов{'о' if key % 10 == 1 else 'а' if key % 10 in (2, 3, 4) else ''} {round(value * 100 / total_queries, 2)}%')

Задача 4

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

k_max_stats = ''
v_max_stats = 0

for chanel, count in stats.items():
    if count > v_max_stats:
        v_max_stats = count
        k_max_stats = chanel

print(f'Через {k_max_stats} было максимальное число продаж. Количество {v_max_stats}')

# Задача 5
# Попробовать решить через рекурсию
# {'2018-01-01': {'yandex': {'cpc': 100}}}

test_list = ['2018-01-01', 'yandex', 'cpc', 100]
final_dict = dict()

if len(test_list) > 1:
    # test_list.reverse()
    while len(test_list) > 1:     
        x_dict = {test_list[-2]: test_list[-1]}
        del(test_list[-1])
        del(test_list[-1])
        test_list.append(x_dict)
print(x_dict)