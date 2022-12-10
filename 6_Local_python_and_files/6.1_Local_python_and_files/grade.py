# Создайте файл grade.py.
# Напишите в нем функцию get_grade(grade), которая принимает целое число от 2 до 5 и возвращает оценку.

def get_grade(grade):
    if grade == 2:
        return "Плохо"
    if grade == 3:
        return "Удовлетворительно"
    if grade == 4:
        return "Хорошо"
    if grade == 5:
        return "Отлично"
    if grade == "":
        return "Ошибка"

try:
    assert get_grade(2) == "Плохо"
    assert get_grade(3) == "Удовлетворительно"
    assert get_grade(4) == "Хорошо"
    assert get_grade(5) == "Отлично"
    assert get_grade("") == "Ошибка"
except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")
else:
    print("Все хорошо, все работает")