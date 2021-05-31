# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
subjects = dict()
file_name = "text_6.txt"
try:
    with open(file_name, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.replace(":", "").replace("-", "").replace("(пр)", "").replace("(л)", "").replace("(лаб)", "")
            lst = line.split()
            subject_name = lst[0]
            subject_sm = 0
            for i in range(1, len(lst)):
                subject_sm += int(lst[i])
            subjects.update({subject_name: subject_sm})
except FileNotFoundError:
    print(f"Не найден файл '{file_name}'")

print(subjects)