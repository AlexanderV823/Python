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

# Задача 2

cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',  
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],  
      ]
  ]
]

person = int(input('На сколько человек рассчитать ингредиенты? '))

for name_dish, compound in cook_book:
    print(f'{name_dish.title()}:')
    for ingredient, weight, unit in compound:
        print(f'{ingredient}, {weight * person}{unit}')
    print()