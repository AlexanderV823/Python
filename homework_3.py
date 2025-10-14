# Задача 1

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()

    pairs = zip(boys, girls)

    print(f'Идеальные пары:')

    for boy, girl in pairs:
        print(f'{boy} и {girl}')
else:
    print(f'Количество людей в списках не совпадает!')
    