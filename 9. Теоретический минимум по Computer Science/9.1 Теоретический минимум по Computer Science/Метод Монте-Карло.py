names = ["Кларисса", "Мелисса", "Лариса", "Алиса", "Лариса", "Мама Бориса"]

def look_for_alice(names):

    found = False
    for name in names:
        if name == "Алиса":
           found = True
    return found


print(look_for_alice(names))