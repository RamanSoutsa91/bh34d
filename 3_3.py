# Решение задачи на форматирование строк 3 способами
name = input('Your name: ')
age = input('Your age: ')
city = input('Your city: ')
text = 'Your name ' + name + ', your age ' + str(age) + ', your city ' + city
print(text)

name = input('Your name: ')
age = int(input('Your age: '))
city = input('Your city: ')
text2 = 'Hello. Your name %s, your age %d, your city %s' % (name, age, city)
print(text2)

name = input('Your name: ')
age = int(input('Your age: '))
city = input('Your city: ')
text3 = 'Hello. Your name {}. Your age {}. Your city {}.' .format(name, age, city)
print(text3)

name = input('Your name: ')
age = int(input('Your age: '))
city = input('Your city: ')
text4 = f'Hello. Your name {name}, your age {age}, your city {city}.'
print(text4)
