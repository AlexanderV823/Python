# Работа с файлами

# Чтение

def is_closed(file):
    if file.closed: # Функция .closed возвращает статус закрытия
        print(f'Файл {file} закрыт')
    else:
        print(f'Файл {file} открыт')

# file_1 = open('test.txt') 

# data = file_1.read()

# print(data)

# file_1.close() # После работы файл нужно обязательно закрыть

# with open('test.txt') as file_2: # При такой конструкции файл сам закроется, когда уйдет отступ
#     data_2 = file_2.read()
#     print(data_2)
#     is_closed(file_2) # Здесь еще файл открыт

# is_closed(file_2) # Здесь уже файл закрыт

# Большие файлы нужно читать построчно.
# Открытый файл, может не поместиться в оперативную память

with open('test.txt') as file_3: # При такой конструкции файл сам закроется, когда уйдет отступ
    print(f'Печатаем последовательным вызовом {file_3.readline().strip()}') # strip() удаляет перевод строки
    print(f'Печатаем последовательным вызовом {file_3.readline().strip()}') # каждый последующий вызов выводит очередную строку
    print(f'Печатаем последовательным вызовом {file_3.readline().strip()}') # каждый последующий вызов выводит очередную строку

    print(f'После перебора всех строк {is_closed(file_3)}')  

    lines_list = file_3.readlines()

    # print(f'Печатаем строку по индексу [2] {lines_list[2]}')
    
    print(f'После перебора всех строк {is_closed(file_3)}')  

    for line in lines_list:
        print(f'Печатаем строку перебором из списка строк {line.strip()}')

    for line in file_3:
        print(f'Печатаем напрямую перебором строк из файла {line.strip()}')

    print(f'После перебора всех строк {is_closed(file_3)}')

print(f'А здесь')
is_closed(file_3)

# Запись

with open('test.txt', 'a') as file_3: # По умолчанию файл открывается только для чтения. Атрибут a  добавляет строки в конец
    file_3.write('Hello, Sanek!\n') # При каждом новом вызове дописвается эта строка
    # print(f'Печатаем последовательным вызовом {file_3.readline().strip()}') # При открытии файля для записи, читать нельзя

with open('test.txt') as file_3:

    for line in file_3:
        print(f'Печатаем напрямую перебором строк из файла {line.strip()}')

with open('test.txt', 'w') as file_3: # Атрибут w перезаписывает
    file_3.write('All rewriteble\n') # При каждом новом вызове дописвается эта строка
    # print(f'Печатаем последовательным вызовом {file_3.readline().strip()}') # При открытии файля для записи, читать нельзя

with open('test.txt') as file_3:

    for line in file_3:
        print(f'Печатаем напрямую перебором строк из файла {line.strip()}')

with open('test.txt', 'rb') as file_3: # Можно передать второй атрибут b чтобы прочитать байты, а не такст 't' по умолчанию
    print('Напечатаем байты:')
    print(file_3.read())

import os

print(os.getcwd()) # Сообщает текущий каталог

with open('test.txt', 'w', encoding='cp1251') as file_3: # Атрибут w перезаписывает
    file_3.write('Привет, Санек!\n') # При каждом новом вызове дописвается эта строка

with open('test.txt') as file_3: # Открываем по умолчанию для чтения и в кодировке UTF-8
    lines_list = file_3.readlines()
    print(f'По умолчанию в UTF-8: {lines_list[0]}')

with open('test.txt', 'r', encoding='cp1251') as file_3:
    lines_list = file_3.readlines()
    print(f'Выбрав нужную кодировку можем прочитать кириллицу {lines_list[0]}')