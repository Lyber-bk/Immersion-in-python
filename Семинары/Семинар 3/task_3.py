# ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка. ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

# ✔Создайте вручную кортеж содержащий элементы разных типов. ✔Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

# ✔Создайте вручную список с повторяющимися элементами. ✔Удалите из него все элементы, которые встречаются дважды.


list1 = [1, 1, 2, 3, 4, 4, 5, 6, 4, 7, 7, 6]
for item in set(list1):
    if list1.count(item) == 2:
        list1.remove(item)
        list1.remove(item)


# ✔Создайте вручную список с повторяющимися целыми числами. ✔Сформируйте список с порядковыми номерами нечётных элементов исходного списка. ✔Нумерация начинается с единицы.

lst1 = [1,2,2,3,4,4,4,5,6,77,7,7]
lst2 = []
for i, item in enumerate(lst1, 1):
    if item % 2:
        lst2.append(i)
print(lst2)

# Пользователь вводит строку текста. Вывести каждое слово с новой строки. ✔Строки нумеруются начиная с единицы. ✔Слова выводятся отсортированными согласно кодировки Unicode. ✔Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

from string import punctuation

text = 'Питон самый! луч\nший яз-ык в мире. Это точ?но'

# for ch in punctuation:
#     text = text.replace(ch, '')

word = ''
text_clean = []
for ch in text.lower():
    if ch.isalpha():
        word += ch
    elif ch == ' ':
        text_clean.append(word)
        word = ''
text_clean.append(word)
text = sorted(text_clean)
max_len = len(max(text, key=len))

for i, word in enumerate(text, 1):
    print(f'{i}. {word:.>20}')

# ✔Пользователь вводит строку текста. ✔Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним. ✔Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке. ✔Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

text = 'Питон самый! луч\nший яз-ык в мире. Это точ?но'

word = ''
text_clean = []
for ch in text.lower():
    if ch.isalpha():
        word += ch
    elif ch == ' ':
        text_clean.append(word)
        word = ''
text_clean.append(word)
text = ' '.join(text_clean)

dict_count = {}
dict_self = {}

for ch in set(text):
    dict_count[ch] = text.count(ch)
print(dict_count)

# for ch in text:
#     if ch in dict_self:
#         dict_self[ch] += 1
#     else:
#         dict_self[ch] = 1

for ch in text:
    dict_self[ch] = dict_self.get(ch, 0) + 1
print(dict_self)

print(dict_count == dict_self)

python
def count_letters(text):
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

text = input("Введите строку текста: ")
result = count_letters(text)
print(result)

