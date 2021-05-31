# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
try:
    file_name = "text_3.txt"
    with open(file_name, mode="r", encoding="utf-8") as f:
        cnt = 0
        salary_all = 0
        print("---------------------------------------------------")
        print("Список сотрудников с окладом менее 20 тыс.:")
        for line in f:
            try:
                words = line.split()
                name = words[0]
                salary = float(words[1])
                if salary < 20000:
                    print(f"{name} {salary}")
                salary_all += salary
            except ValueError:
                print(f"Ошибка при преобразовании оклада '{words[1]}' сотрудника '{name}' к float")
                exit()
            except IndexError:
                print(f"Ошибка при разборе строки '{line}'. Не хватает данных")
                exit()
        print("---------------------------------------------------")
        print(f"Средняя величина дохода сотрудников = {salary_all}")
except FileNotFoundError:
    print(f"Не найден файл '{file_name}'")
