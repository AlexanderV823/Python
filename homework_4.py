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
