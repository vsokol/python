# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def print_user_data(first_name, last_name, year_of_birth, email, phone):
    print("Имя - {}, Фамилия - {}, год рождения - {}, email - {}, телефон - {}".format(first_name, last_name,
                                                                                       year_of_birth, email, phone))


str_fio = input("Введите фамилию и имя через пробел: ")
list_fio = str_fio.split(" ")
last_name = list_fio[0]
first_name = list_fio[1]
year_of_birth = input("Введите год рождения: ")
email = input("Введите email: ")
phone = input("Введите телефон: ")

print_user_data(last_name=last_name, first_name=first_name, year_of_birth=year_of_birth, email=email, phone=phone)
