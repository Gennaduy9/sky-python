from pin import check_pin

print("Введите ваш ПИН-код")
user_input = input()

if not check_pin(user_input):
    print("Такой ПИН-код НЕ подходит")

else:
    print("Такой ПИН-код подходит")