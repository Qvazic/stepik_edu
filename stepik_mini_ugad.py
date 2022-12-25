import random as r


def is_valid(num):
    return 0 < num < 100


numbers = r.randrange(100)
print('Добро пожаловать в числовую угадайку')
count = 0
while True:
    n = int(input('Введите число от 1 до 100: '))
    if is_valid(n):
        if n == numbers:
            print(f'Вы угадали за {count} попыток, поздравляем!')
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif n > numbers:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif n < numbers:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
