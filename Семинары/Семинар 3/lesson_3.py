# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}.
# Достаточно вернуть один допустимый вариант.
#
import decimal


def backpack_(items, max_weight):
    backpack = {}

    total_weight = 0

    for item, weight in items.items():
        if total_weight + weight <= max_weight:
            backpack[item] = weight
            total_weight += weight

    return backpack

items = {"ключи": 0.3,
         "кошелек": 0.2,
         "телефон": 0.5,
         "зажигалка": 0.1}
max_weight = 1

print(backpack_(items, max_weight))

# или другой вариант
from decimal import Decimal
backpack = {}

for item, weight in items.items():
    if Decimal(weight) <= Decimal(max_weight):
        backpack[item] = round(weight, 1)
        max_weight -= Decimal(weight)

print(backpack)

# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

import re
from collections import Counter

text = "Пример текста с числами 123 и знаками препинания!? Example text with numbers 123 and punctuation marks!"


def count_words(text):
    # Приведение текста к нижнему регистру и удаление знаков препинания
    text = text.lower()
    text = re.sub(r'[^а-яА-ЯёЁa-zA-Z]', ' ', text)
    # регулярное выражение удалит все знаки препинания, числа и пробелы из текста.
    # Если вам нужно сохранить пробелы между словами,
    # вы можете изменить регулярное выражение на [^а-яА-ЯёЁa-zA-Z\s]
    # Разделение текста на слова
    words = text.split()

    # Подсчет количества вхождений слов
    word_counts = Counter(words)

    # Сортировка словаря по значениям в убывающем порядке
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Возвращение первых 10 элементов отсортированного словаря
    return sorted_word_counts[:10]


# или


import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)


# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# # Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# # Результат должен быть в виде словаря с вещами в рюкзаке:{предмет:вес}
# # *Верните все возможные варианты комплектации рюкзака.


from pprint import pprint # Эта строка импортирует функцию pprint из модуля pprint. pprint
# используется для более читаемого вывода сложных структур данных, таких как списки и словари.

items = {'sleeping bag': 5, 'tent': 10, 'water bottle': 2, 'food': 6}
max_weight = 15
backpacks = []

for i in range(2**len(items)): # Запускается цикл for, который будет перебирать все числа
    # от 0 до 2^количество_предметов минус 1.
    # Это используется для создания всех возможных комбинаций предметов в рюкзаке.
    backpack = {}
    weight = 0
    for j, item in enumerate(items): # Запускается вложенный цикл for, который перебирает
        # предметы и их индексы в словаре items с помощью enumerate.
        if i & (1 << j):
            if weight + items[item] <= max_weight: # Здесь проверяется, не превышает ли
                # суммарный вес текущей комбинации максимальный вес рюкзака.
                backpack[item] = items[item] # Если условие выполняется, то предмет
                # добавляется в backpack, и его вес прибавляется к переменной weight.
                weight += items[item]
            else:
                break # Если максимальный вес рюкзака превышен, то цикл завершается,
                # чтобы не проверять более длинные комбинации.
    backpacks.append(backpack) # После завершения внутреннего цикла, текущая комбинация
    # предметов добавляется в список backpacks.

result = [backpack for backpack in backpacks if backpack] # Здесь создается список result,
# который фильтрует backpacks, чтобы исключить пустые комбинации (комбинации, которые не
# укладываются в рюкзак). Таким образом, result содержит все возможные варианты комплектации рюкзака.

pprint(result)


# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def find_duplicates(lst):
    # Создаем пустой список для повторяющихся элементов
    duplicates = []

    # Создаем пустой сет для отслеживания уникальных элементов
    unique_set = set()

    # Итерируемся по элементам исходного списка
    for item in lst:
        # Если элемент уже был в уникальном сете, значит, он повторяется
        if item in unique_set:
            duplicates.append(item)
        else:
            unique_set.add(item)  # Добавляем элемент в уникальный сет

    return set(duplicates)

# Пример использования:
input_list = [1, 1,1,1,1,1,1]
result = list(find_duplicates(input_list))

print(result)