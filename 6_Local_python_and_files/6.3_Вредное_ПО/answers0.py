user_language = input("Какой язык вы учите?")
user_tiem = input("Как давно?")
user_institution = input("Где?")


with open('answers0.txt', 'w', encoding='utf-8') as file:
    file.write(f"{user_language}\n")
    file.write(f"{user_tiem}\n")
    file.write(f"{user_institution}\n")

print("Ответы записаны!")



print("Я вирус!")
