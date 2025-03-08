# https://letpy.com/handbook/string-methods/

text = "Hello, World!"
print(type(text))  # <class 'str'>

# Конкатенация строк
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World

# Многострочная строка
multiline_text = """Это
многострочная
строка"""
print(multiline_text)


# Разделение строки по пробелам
text1 = "Hello World Python"
words = text1.split()
print(words)  # ['Hello', 'World', 'Python']

# Разделение по запятой
data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']


# Приведение к верхнему и нижнему регистру
text2 = "Hello World"
print(text2.upper())  # HELLO WORLD
print(text2.lower())  # hello world

# Удаление пробелов с начала и конца строки
text3 = "   Hello World   "
print(text3.strip())  # Hello World

print("Hello Andrey")


'''----------------------------------------------------------------------------------------'''
'''   0123456789'''
test='test привет!'


print(test[0])
print(test[1:3])
print(test[:2])
print(test[2:])

text4 = "Привет, мир!"
substring = "мир"

# Проверка наличия подстроки
if substring in text4:
    print(f'Подстрока "{substring}" найдена в строке.')
else:
    print(f'Подстрока "{substring}" не найдена в строке.')
'''----------------------------------------------------------------------------------------'''


text5 = "Программирование — это искусство создания программ."
substring2 = "пр"

# Подсчет количества вхождений подстроки
count = text5.count(substring2)
print(f'Подстрока "{substring2}" встречается в строке {count} раз(а).')

'''----------------------------------------------------------------------------------------'''
