filename = "user_data.txt"

f = open(filename, "r", encoding='utf-8')
name = f.readline()
name = name.replace("\n", "")
surname = f.readline()
surname = surname.replace("\n", "")
email = f.readline()
email = email.replace("\n", "")
phone = f.readline()
phone = phone.replace("\n", "")


print(f"{name} {surname} – это вы. Ваша почта {email}, ваш телефон {phone}")