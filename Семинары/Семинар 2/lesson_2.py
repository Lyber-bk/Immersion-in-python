# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
#
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


HEX_BASE = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']


numbers = int(input('Введите число: '))
print(hex(numbers)[2:])
numbers_hex = ''

while numbers > 0:
    num = numbers % HEX_BASE
    numbers_hex = str(hex_data[num]) + numbers_hex
    numbers //= HEX_BASE

print(numbers_hex)

# ✔ Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

f1 = Fraction(fraction1)
f2 = Fraction(fraction2)
print(f1 + f2, f1 * f2)

num1, denom1 = map(int, fraction1.split("/"))
num2, denom2 = map(int, fraction2.split("/"))

# Находим НОД (наибольший общий делитель) для знаменателей
a, b = denom1, denom2
while b:
    a, b = b, a % b
gcd_denom = a

# Находим НОК (наименьшее общее кратное) для знаменателей
lcm_denom = denom1 * denom2 // gcd_denom

# Находим сумму дробей
num_sum = num1 * (lcm_denom // denom1) + num2 * (lcm_denom // denom2)

# Находим произведение дробей
num_product = num1 * num2
denom_product = denom1 * denom2

print("Сумма дробей:", str(num_sum) + "/" + str(lcm_denom))
print("Произведение дробей:", str(num_product) + "/" + str(denom_product))

