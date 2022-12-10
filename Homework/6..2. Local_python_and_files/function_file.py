import random

def load_words(filename):

    '''
    Функция вызывает данные пользователя.
    :param filename: загружает слова.
    :return: вызывает список слов.
    '''

    new_list = []

    with open(filename, 'r', encoding='utf-8') as f:
        for list_i in f.readlines():
            new_list.append(list_i.strip('\n'))
    return new_list

def get_word(word):

    '''
    Функция выбирает первое слово из списка, перемешивает буквы и предлагает пользователю его отгадать.
    :param word: список слов до объединения букв в списке.
    :return: вызывает перемешанные буквы списка.
    '''

    word = list(word)
    random.shuffle(word)
    return f"Угадайте слово: {' '.join(word)}\n"

# Выводим статистику с помощью функции.
def write_history(filename, user_name,  total_score):
    with open(filename, "a", encoding='utf-8') as f:
        f.write(f"{user_name} {total_score}\n")

# Статистика
def read_history(filename):
    max = 0
    count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for list_i in f.readlines():
            count += 1
            total_score = int(list_i.split(' ')[1])
            if total_score > max:
                max = total_score

    return f"\nВсего игр сыграно: {count}\n" \
           f" Максимальный рекорд: {max}"