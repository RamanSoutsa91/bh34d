# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
# Первое решение
result = input('Введите любое предложение:')
print(result.replace(' ', ' - '))

# Второе решение
text = input('Напишите ваше ФИО: ')
words = text.split(' ')
text = ' - '.join(words)
print(text)
