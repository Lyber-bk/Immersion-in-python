# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):  # Получаем количество строк и столбцов в матрице
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    transposed = [[0 for _ in range(rows)] for _ in range(cols)]  # Создаем новую матрицу с обратными размерами
    # (столбцы становятся строками и наоборот)

    for i in range(rows):  # Заполняем новую матрицу значениями из исходной с учетом транспонирования
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# Пример использования:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose_matrix(matrix)

# Выводим результат
for row in transposed_matrix:
    print(row)


# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def create_dict(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        dict[str(value)] = key
    return dict


arguments = create_dict(arg1=10, arg2="hello", arg3=True)
print(arguments)

# Возьмите задачу о банкомате из семинара.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

START_BALANCE = 0
DEPOSIT_FACTOR = 50

balance = START_BALANCE
operations = []


def deposit_account(balance):
    amount = int(input(f'Введите сумму для пополнения кратную {DEPOSIT_FACTOR}: '))
    if amount > 0 and amount % DEPOSIT_FACTOR == 0:
        balance += amount
        operations.append(f'Пополнение {amount}')
        print(f"Баланс пополнен на {amount}. Текущий баланс: {balance}")
    else:
        print(f'Сумма пополнения не кратна {DEPOSIT_FACTOR}')
        print(f'Текущий баланс: {balance}')
    return balance


def withdraw_account(balance):
    amount = int(input(f'Введите сумму для снятия кратную {DEPOSIT_FACTOR}: '))
    if amount > 0 and amount % DEPOSIT_FACTOR == 0:
        balance -= amount
        operations.append(f'Снятие {amount}')
        print(f"Сумма {amount} снята. Текущий баланс: {balance}")
    else:
        print(f'Сумма снятия не кратна {DEPOSIT_FACTOR}')
        print(f'Текущий баланс: {balance}')
    return balance


while True:
    action = input(f'Для работы с банкоматом выберите действие:\n1 - пополнить\n2 - снять\n3 - выйти\n')
    match action:
        case '1':
            balance = deposit_account(balance)
        case '2':
            balance = withdraw_account(balance)
        case '3':
            print(f'Баланс вашего счета: {balance:.0f}')
            break
        case _:
            break

print(operations)