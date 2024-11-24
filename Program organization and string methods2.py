# перенесена команда int с 4 строки на 5, можно использовать оба варианта.
name = input('Введите ваше имя: ')
current_year = 2024
dateOfBurth = input('В каком году Вы родились? ')
age = current_year - int(dateOfBurth)
print('Здравствуйте,',name)
print('В этом году Вам', age, 'лет')