from pprint import pprint
import os

cook_book = dict()

# Задача 1
def add_cook_book(file_name: str):
    if os.path.exists(file_name) and os.path.isfile(file_name):
        with open(file_name, 'r', encoding='UTF-8') as file:      
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
    else:
        print("Файл не найден")

# Задача 2
def print_ingridients(dishes: list, persons: int):
    ingridients_dict = dict()
    for dish in dishes:
        if cook_book.get(dish) is None:
            print(f'Блюда {dish} нет.')
        else:
            ingridients_list_of_dict = cook_book.get(dish)
            for ing_dict in ingridients_list_of_dict:
                ingredient_name = ing_dict.get('ingredient_name')
                measure = ing_dict.get('measure')
                quantity = ing_dict.get('quantity')
                if ingridients_dict.get(ingredient_name) is None:                    
                    ingridients_dict.setdefault(ingredient_name, {'measure': measure, 'quantity': quantity * persons})
                else:
                    ingridient_old = ingridients_dict.get(ingredient_name)
                    quantity_old = ingridient_old.get('quantity')
                    ingridients_dict[ingredient_name] = {'measure': measure, 'quantity': quantity_old + (quantity * persons)}             
    print(f'Список ингредиентов:')
    pprint(ingridients_dict)            

def print_help():
    print(f'a, add – чтение в файла с рецептами.')
    print(f'с, calc – расчет количества ингридиентов.')
    print(f'h, help – вывод подсказки')
    print(f'q, quit – выход из программы')

def main():
    while True:
        user_input = input('Введите команду: ')
        if user_input == 'a' or user_input == 'add':
            add_cook_book(str(input('Введите имя файла: ')))
        elif user_input == 'c' or user_input == 'calc':
            dish_string = str(input('Введите через запятую названия блюд: '))
            persons = int(input('Введите количество персон: '))
            print_ingridients(dish_string.split(', '), persons)
        elif user_input == 'h' or user_input == 'help':
            print_help()
        elif user_input == 'q' or user_input == 'quit':
            break
        else:
            print(f'Указана не существующая команда. Для вызова справки введите "h"')

main()