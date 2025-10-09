#  Операции сравнения. Возвращаемое значение булево
print(2 > 1) #  Больше, True
print(2 < 1) #  Меньше, False
print(2 == 1) #  Равно! однинарный знак = это оператор присваивания, False
print(2 != 1) #  Не равно, True
print(2 >= 1) # Больше или равно, True
print(2 <= 1) # Меньше или равно, False

print('b' < 'a') #  Можно сравнивать строки, сравнение по порядковому номеру символа, False
print('A' < 'a') #  True 

print(True and True) # True 
print(True and False) #  False 
print(True or False) #  True
print(not True) #  False

print(bool(0)) #  False
print(bool(1)) #  True, любое число кроме 0, будет Истина
print(bool('')) #  False
print(bool('Hello, world!')) #  True, любая не пустая строка, будет Истина

#  Условные конструкции
# if - Если
# elif - ИначеЕсли
# else - Иначе
print('Введите два числа для сравнения:')
a = int(input('Число a: '))
b = int(input('Число b: '))

if a == 6 and b == 9:
    print('Oh, my!')
elif a < b:
    print('a меньше b')
elif a > b:
    print('a больше b')
else:
    print('a равно b')

user_name = input('Как Вас зовут? ')

if user_name:
    print('Привет,', user_name, '!')
else:
    print('Привет, незнакомец!')