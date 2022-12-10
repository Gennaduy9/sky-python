"""
Написать программу которая будет вести
учёт покупок и расходов.

Программа при запуске выводит список
расходов и общую сумму по ним.

Программа: В списке 7 позиций. Сумма 2600 Р
"""

row_index = 0
items_count = 0
items_sum = 0

with open('shopping_list.txt', encoding='utf-8') as file:
    for item_data in file:
        row_index += 1
        if item_data.count(':') < 2:
            print(f"В стороке {row_index} есть ошибка")
            continue

        item, quantity, price = item_data.strip().split(':')
        items_count += 1
        items_sum += int(price) * int(quantity)

print(f"В списке {items_count} позиций. Сумма {items_sum} Р")




