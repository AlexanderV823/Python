# Задача 1

def read_cook_book():

    file = open('recipes.txt')
    
    cook_book = dict()

    lines_list = file.readlines()

    for index, line in enumerate(lines_list):
        if line:
            if isinstance(line, str) and isinstance(lines_list[index::1], int):
                dish = line.strip()
                print(dish)
                ingrdnt_list = list()
                first_ingrdnts_index = index + 2
                print(first_ingrdnts_index)
                while first_ingrdnts_index <= lines_list[index + 1]:
                    print(first_ingrdnts_index)
                    ingredients = lines_list[first_ingrdnts_index].split(' | ') 
                    print(ingredients)            
                    ingrdnt_list.append({'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]})
                    cook_book.setdefault(dish, ingrdnt_list)
    print(cook_book)

read_cook_book()