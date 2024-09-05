import random # пусть клетки выбираются случайно ( для 2 задания )

#ur1 Пусть пользователь сам задает числа
num1 = int(input('Введите число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if num1==num2==num3: # Проверка выполнения условия равенства 3
	print('3 Числа равны')
elif num1==num2 or num1==num3 or num2==num3: # # Проверка выполнения условия равенства 2
	print('2 Числа равны')
else:
	print('0 Чисел равны')


#ur 2
numst1 = random.randint(1,8) # Случайные 2 числа для столбцов
numst2 = random.randint(1,8)
numstr1 = random.randint(1,8) # Случайные 2 числа для строк
numstr2 = random.randint(1,8)
if numst1 == numst2 or numstr1 == numstr2: # ладья сможет сходить только если совпадает вертикаль или горизонталь
	print('YES')
else:
	print('No')

#ur3

Security = False  # Задаем переменной значение False для цикла
while not Security:
    password = input('Введите пароль из 8 символов, строчных и заглавных букв: ')  # Ввод пароля
    if (len(password) < 8 or 
        not any(c.isupper() for c in password) or 
        not any(c.islower() for c in password) or 
        not any(c.isdigit() for c in password)):  # Делаем проверку всех условий безопасности
        print('Недостаточная безопасность пароля, попробуйте еще') 
    else:
        print('Пароль безопасный')
        Security = True  # Выход из цикла