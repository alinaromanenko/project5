letter_list = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'А', 'О', 'И', 'Е', 'Ё', 'Э', 'Ы', 'У', 'Ю', 'Я']

answer = input('Нужно ли перевести фразу? ')
while answer.lower() == 'да':
    letter = input('Введите первую букву цвета языка: ')
    text = input("Введите текст: ")
    for i in letter_list:
        char = i+letter+i.lower()
        text = text.replace(i, char)
    print(text)
    answer = input('Нужно ли перевести фразу? ')


answer_ = input('Хотите ли вы воспользоваться переводчиком? ')
while answer_.lower() == 'да':
    letter = input('Введите первую букву цвета языка: ')
    text = input("Введите текст: ")
    for i in letter_list:
        char = i+letter+i.lower()
        text = text.replace(char, i)
    print(text)
    answer_ = input('Хотите ли вы воспользоваться переводчиком? ')