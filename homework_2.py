# #  Задача 2
print('Укажите данные призывника')
age = (int(input('Возраст: ')))
height = (int(input('Рос: ')))
child = int(input('Количество детей: '))
study = bool(input('Студент (Да/Нет): '))

if age > 18 and not(study) and child < 4:
    if height < 180:
        print('Танкист или подводник')
    else:
        print('Другие войска')
else:
    print('Не годен к призыву')

# Задача 3
day = int(input('Введите дату рождения: '))
mounth = int(input('Введите месяц рождения: '))

if 0 < day <= 31 and 0 < mounth <= 12:
    if ((day >= 21) and mounth == 3) or ((day <= 20) and mounth == 4):
        print('Вы Овен')
    elif ((day >= 21) and mounth == 4) or ((day <= 20) and mounth == 5):
        print('Вы Телец')
    elif ((day >= 22) and mounth == 5) or ((day <= 21) and mounth == 6):
        print('Вы Близнецы')
    elif ((day >= 22) and mounth == 6) or ((day <= 22) and mounth == 7):
        print('Вы Рак')
    elif ((day >= 23) and mounth == 7) or ((day <= 21) and mounth == 8):
        print('Вы Лев')
    elif ((day >= 22) and mounth == 8) or ((day <= 23) and mounth == 9):
        print('Вы Дева')
    elif ((day >= 24) and mounth == 9) or ((day <= 23) and mounth == 10):
        print('Вы Весы')
    elif ((day >= 24) and mounth == 10) or ((day <= 22) and mounth == 11):
        print('Вы Скорпион')
    elif ((day >= 23) and mounth == 11) or ((day <= 22) and mounth == 12):
        print('Вы Стрелец')
    elif ((day >= 23) and mounth == 12) or ((day <= 20) and mounth == 1):
        print('Вы Козерог')    
    elif ((day >= 21) and mounth == 1) or ((day <= 19) and mounth == 2):
        print('Вы Водолей')
    elif ((day >= 20) and mounth == 2) or ((day <= 20) and mounth == 3):
        print('Вы Рыбы')
    else:
        print('Вы ввели числа вне диапазана дат')
else:
    print('Вы ввели числа вне диапазана дат')