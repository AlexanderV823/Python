#  Вычисление площади
def calc_area(length_a, length_b):
      return length_a * length_b

#  Вычисление периметра
def calc_perimeter(length_a, length_b):
      return 2 * (length_a + length_b)

# Вывод результата
def print_message(str_perimeter, str_area):
        print(f'Вывод:')
        print(f'Периметр: {str_perimeter}')
        print(f'Площадь: {str_area}')

# Вывод расчета
def print_calc(credit_cost, accumulation):
        print(f'Вывод:')
        print(f'За год потрачено на кредиты : {credit_cost}')
        print(f'Накоплено за год: {accumulation}')

#  Попытка
try:
      length_ab = float(input('Введите длину стороны квадрата: '))

      if length_ab > 0:  
            perimeter = calc_perimeter(length_ab, length_ab)
            area = calc_area(length_ab, length_ab)
            print_message(perimeter, area)
      else:
            print('Введите положительные числа!')
#  Исключение
except ValueError:
      print('Введены не числовые значения!') 
                 
try:
      length_a = float(input('Введите длину прямоугольника: '))
      length_b = float(input('Введите ширину  прямоугольника: '))

      if length_a > 0 and length_b > 0:  
            perimeter = calc_perimeter(length_a, length_b)
            area = calc_area(length_a, length_b)
            print_message(perimeter, area)
      else:
            print('Введите положительные числа!')
except ValueError:
      print('Введены не числовые значения!')

try:
      mounth_salary = float(input('Введите заработную плату в месяц: '))
      credit_percent = int(input('Какой процент от зарплаты уходит на погашение кредитов? '))
      life_percent = int(input('Какой процент от зарплаты уходит бытовые траты? '))

      if mounth_salary > 0:  
            year_credit_cost = (mounth_salary * credit_percent / 100) * 12
            year_accumulation = mounth_salary * 12 - ((mounth_salary * life_percent / 100) * 12 + year_credit_cost) 
            print_calc(year_credit_cost, year_accumulation)
      else:
            print('Введите положительные числа!')
#  Исключение
except ValueError:
      print('Введены не числовые значения!')