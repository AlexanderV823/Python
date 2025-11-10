# Задача 1
from pprint import pprint

def print_cook_book():
    cook_book = dict()
    with open('recipes.txt', 'r', encoding='UTF-8') as file:      
        line = file.readline().strip()
        while line:
                try:
                    dish = line
                    count_ingredients = int(file.readline().strip())
                    ingredients = list()
                    for _ in range(count_ingredients):
                        ingredient_string = file.readline().strip()
                        ingredient_summary = ingredient_string.split(' | ')
                        ingredient_info = {'ingredient_name': ingredient_summary[0], 'quantity': int(ingredient_summary[1]), 'measure': ingredient_summary[2]}
                        ingredients.append(ingredient_info)
                    cook_book.setdefault(dish, ingredients)
                    line = file.readline().strip()  # Здесь возникает пустая строка, если ее здесь не перескочить, то условие прервется раньше конца файла
                    line = file.readline().strip()
                except ValueError:
                    line = file.readline().strip()       
    pprint(cook_book)

print_cook_book()