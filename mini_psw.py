import random as rnd


def exception_psw(t_psw):
    t_psw = str(t_psw)
    exception_chars = "il1Lo0O"
    for t in exception_chars:
        t_psw = t_psw.replace(t, "")

    return t_psw


def gen_psw(lenght, chars_psw):
    psw = ""
    for _ in range(lenght):
        psw += rnd.choice(chars_psw)
    return psw


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'

chars = ""

n_psw = int(input("Количество паролей для генерации? "))
len_psw = int(input("Укажите длину одного пароля? "))
if input('Включать ли цифры 0123456789?(д) ') == "д": chars += digits
if input('Включать ли прописные буквы?(д) ') == "д": chars += uppercase_letters
if input('Включать ли строчные буквы?(д) ') == "д": chars += lowercase_letters
if input('Включать ли символы: !#$%&*+-=?@^_ ?(д) ') == "д": chars += punctuation
if input('Исключать ли неоднозначные символы il1Lo0O?(д) ') == "д": chars = exception_psw(chars)

for _ in range(n_psw):
    print(gen_psw(len_psw, chars))
