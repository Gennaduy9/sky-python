# Создайте файл palindrome.py. В нем — функцию is_palindrome(word).
# Функция должна возвращать True, если слово палиндром, иначе — False.
# Чтобы проверить, является ли строка палиндромом, уберите из нее пробелы, приведите к нижнему регистру,
# затем проверьте, что инвертированная строка (reversed_str = str[::-1]) равна оригинальной строке.

def is_palindrome(word):
    return word == word[::-1]

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")




