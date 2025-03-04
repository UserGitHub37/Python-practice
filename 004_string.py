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

