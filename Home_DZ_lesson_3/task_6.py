#ДЗ_6
'''
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
'''
words = input()
def int_func(word):
    return words.capitalize()
print(int_func(word = words))
