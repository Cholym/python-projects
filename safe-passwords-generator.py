import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstyvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTYVWXYZ'
symbols = '!#$&*+-=?@^_'
chars = ''

passwords_quantity = int(input('Сколько паролей сгенерировать? '))
passwords_length = int(input('Укажите длину одного пароля '))
include_numbers = input('Включить ли цифры? ')
include_upper_case = input('Включить ли прописные буквы? ')
include_lower_case = input('Включить ли строчные буквы? ')
include_symbols = input('Включить ли символы? ')
exclude_ambiguous = input('Исключить ли неоднозначные символы типа il1Lo0O? ')

def generate_password(length, chars):
    password = random.sample(chars, length)
    print(*password, sep = "")

for _ in range(passwords_quantity):
    if include_numbers == "да":
        chars += digits
    if include_upper_case == "да":
        chars += uppercase_letters
    if include_lower_case == "да":
        chars += lowercase_letters
    if include_symbols == "да":
        chars += symbols
    if exclude_ambiguous == "да":
        for i in "il1Lo0O":
            chars.replace(i,"")
    generate_password(passwords_length, chars)
    