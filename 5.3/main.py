import keyboard

# Wczytujemy dane pracownika
first_name = keyboard.input_string('Podaj imię: ')
last_name = keyboard.input_string('Podaj nazwisko: ')
age = keyboard.input_integer('Podaj wiek: ')
salary = keyboard.input_real('Podaj pensję: ')
is_salary_hidden = keyboard.input_boolean('Ukryć pensję? (y/n): ')

# Wyświetlamy dane
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', salary)