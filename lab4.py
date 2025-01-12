# Задание 1
import math
import datetime

number = 16
sqrt_value = math.sqrt(number)
print(f"Квадратный корень из {number} равен {sqrt_value}")

current_datetime = datetime.datetime.now()
print(f"Текущая дата и время: {current_datetime}")

# Задание 2
def add(a, b):
    return a + b

result = add(5, 3)
print(f"Сумма 5 и 3 равна {result}")

# Задание 3

def multiply(a, b):
    return a * b

def concatenate(str1, str2):
    return str1 + str2

product = multiply(4, 5)
print(f"Произведение 4 и 5 равно {product}")

concatenated_string = concatenate("Hello, ", "world!")
print(f"Результат конкатенации: {concatenated_string}")