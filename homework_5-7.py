# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

firms = dict()
file_name = "text_7.txt"
profit_all = 0
firm_count = 0
try:
    with open(file_name, mode="r", encoding="utf-8") as f:
        for line in f:
            firm = line.split()
            firm_name = firm[0]
            proceeds = float(firm[2])
            costs = float(firm[3])
            profit = proceeds - costs
            if profit > 0:
                profit_all += profit
            firms.update({firm_name: profit})
            firm_count += 1
except FileNotFoundError:
    print(f"Не найден файл '{file_name}'")

list = [firms, {"average_profit": profit_all / firm_count}]

file_name = "homework_5-7.json"
with open(file_name, mode="w", encoding="utf-8") as f:
    json.dump(list, f, ensure_ascii=False, indent=2)

print(list)