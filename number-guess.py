import random

print('Добро пожаловать в числовую угадайку')

end_num = int(input("До какого числа можно загадать? "))
number = random.randint(1, end_num)
tries_counter = 0

def is_valid(number):
    if end_num >= number >= 1:
        return True
    else:
        return False

while True:
    number_guess = int(input("Угадай, какое число я загадал "))
    if is_valid(number_guess) == False:
        print('А может быть все-таки введем целое число от 1 до', end_num, '?')
        continue
    if number_guess < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        tries_counter += 1
    if number_guess > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
        tries_counter += 1
    if number_guess == number:
        print('Верно!')
        tries_counter += 1
        print('Вы угадали с', tries_counter, "попытки")
        
        answer = input("Сыграем ещё раз? (да/ нет)", )
        if answer == "да":
            end_num = int(input("До какого числа можно загадать? "))
            number = random.randint(1, end_num)
            tries_counter = 0
            continue
        else:
            break
        
print("Спасибо, что играли в числовую угадайку!")