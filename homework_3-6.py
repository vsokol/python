# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().

def int_func(lower_str):
    for char in lower_str:
        if ord(char) < 97 or ord(char) > 122:
            return False, "Символ {} в слове {} не является маленькой латинской буквой".format(char, lower_str)
    str_title = lower_str[0:1].upper() + lower_str[1:]
    return True, str_title

str_input = input("Введите строку состоящую из слов, составленных из маленьких латинских букв: ")
lst = str_input.split()
sentence = ""
for word in lst:
    res, title_word = int_func(word)
    if res:
        sentence = sentence + (" " if len(sentence) != 0 else "") + title_word
    else:
        print(title_word)
        exit()
print(sentence)

