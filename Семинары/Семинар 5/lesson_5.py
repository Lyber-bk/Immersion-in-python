

# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def get_file_info(file_path):
    # Находим последний слэш в строке, разделяющий путь и имя файла
    last_slash_index = file_path.rfind("/")
    directory = file_path[:last_slash_index+1] if last_slash_index != -1 else ""
    filename = file_path[last_slash_index + 1:]

    # Находим последнюю точку в имени файла, разделяющую имя и расширение
    last_dot_index = filename.rfind(".")
    name = filename[:last_dot_index] if last_dot_index != -1 else ""
    extension = filename[last_dot_index+ 1: ] if last_dot_index != -1 else filename

    # Возвращаем кортеж из трёх элементов
    return (directory, name, "." + extension)


# Пример использования функции
file_path = '/home/user/data/file'
info = get_file_info(file_path)
print(info)

# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
#
# Сумма рассчитывается как ставка умноженная на процент премии.
#
# Не забудьте распечатать в конце результат.

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["13%", "5%", "15%"]

result = {names[i]: round(salary[i] * float(bonus[i].strip('%')) / 100, 2) for i in range(len(names))}
print(result)


# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fibonacci()
for i in range(10):
    print(next(f))