order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for order_convert in order:
    new_order = {
        "count": int(order_convert["skolko"]),
        "specie": order_convert["poroda"].title(),
        "avg_size": order_convert["sred_razmer"] // 10,
    }

    order_converted.append(new_order)

# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
  for key, value in item.items():
      print(key, value)