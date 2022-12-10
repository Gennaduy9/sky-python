from function_file import load_words, get_word, write_history, read_history

# Название файлов с которыми функция работает.
words_txt = "words.txt"
history_txt = "history.txt"

# Программа просит пользователя представиться и запоминает его имя.
print("Введите ваше имя: ")
user_name = input()
words = load_words(words_txt)
total_score = 0

# Основной цикл программы
for word in words:
    print(get_word(word))
    user_answer = input()
    if user_answer.lower().strip(" ") == word:
        print("Верно! Вы получаете 10 очков.")
        total_score += 10
    else:
        print(f"Неверно! Верный ответ – {word}.")

# Вывод результата.
write_history(history_txt, user_name,  total_score)
print(read_history(history_txt))