# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# Первое решение
first_name = input('Ваша фамилия?: ')
second_name = input('Ваше имя?: ')
age = input('Сколько вам лет?: ')
print(first_name, second_name, age, sep=' - ')

# Второе решение
text = input('Напишите ваше ФИО: ')
words = text.split(' ')
text = ' - '.join(words)
print(text)
