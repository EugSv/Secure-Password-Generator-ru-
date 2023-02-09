import random as rnd

def get_info():
    prohibited_symbols = [ a for a in input('Введите через пробел'
                                            ' символы, которые не должен содержать пароль').split()]
    prohibited_numbers = [ a for a in prohibited_symbols if a.isdigit() ]
    prohibited_uppers = [a for a in prohibited_symbols if a.isupper()]
    prohibited_lowers = [a for a in prohibited_symbols if a.islower()]
    prohibited_special_symbs = [a for a in prohibited_symbols if not a.isalnum()]
    pass_amount = input('Сколько паролей нужно сгенерировать?')
    pass_len = input('Какова длина сгенерированного пароля (минимум - 4 символа)?')
    include_special = input('Используем спецсимволы? Напишите 1 или да, если используем.')
    include_digits = input('Используем числа? Напишите 1 или да, если используем.')
    include_lowers = input('Используем заглавные буквы? Напишите 1 или да, если используем.')
    include_uppers = input('Используем строчные буквы? Напишите 1 или да, если используем.')

    return prohibited_numbers,prohibited_uppers,prohibited_lowers,prohibited_special_symbs,\
           pass_amount, pass_len, include_special,include_digits, include_lowers, include_uppers,

def use_special(info0):
    return info0 == 'да' or info0 == '1'


def use_digits(info1):
    return info1 == 'да' or info1 == '1'


def use_uppers(info2):
    return info2 == 'да' or info2 == '1'


def use_lowers(info3):
    return info3 == 'да' or info3 == '1'

def create_password():
    prohnums, prohupps, prohlows, prohsp, amount, leng, inclspec, incldigits, incllowers, incluppers = get_info()
    lowercase_letters = [a for a in 'abcdefghijklmnopqrstuvwxyz' if a not in prohlows]
    uppercase_letters = [a for a in 'abcdefghijklmnopqrstuvwxyz'.upper() if a not in prohupps]
    punctuation = [a for a in '!#$%&*+-=?@^_' if a not in prohsp]
    numbers = [a for a in '1234567890' if a not in prohnums]
    allsymbs = []

    for i in range(int(amount)):
        counter = 0
        password = ''
        if use_special(inclspec) and punctuation:
            counter += 1
            password += punctuation[rnd.randint(0, len(punctuation) - 1)]
            allsymbs += punctuation

        if use_digits(incldigits) and numbers:
            counter += 1
            password += numbers[rnd.randint(0, len(numbers) - 1)]
            allsymbs += numbers

        if use_uppers(incluppers) and uppercase_letters :
            counter += 1
            password += uppercase_letters[rnd.randint(0, len(uppercase_letters) - 1)]
            allsymbs += uppercase_letters

        if use_lowers(incllowers) and lowercase_letters:
            counter += 1
            password += lowercase_letters[rnd.randint(0, len(lowercase_letters) - 1)]
            allsymbs += lowercase_letters

        if not allsymbs:
            print('Чё, бездарь? Захотел ошибку мне вызвать?) Ну уж нет. Иди и нормально набирай значения.')
            return None
        for j in range(int(leng) - counter):
            password += allsymbs[rnd.randrange(0, len(allsymbs)- 1)]
        password = [a for a in password]
        rnd.shuffle(password)
        print(''.join(password))

create_password()
