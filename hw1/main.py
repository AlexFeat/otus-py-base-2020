#!/usr/bin/env python3

from time import time
from functools import wraps


def lead_time(func):
    '''
        Функция декторатор для вывода выремени выполнения функции
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time()
        res = func(*args, **kwargs)
        time_end = time() - time_start
        print('duration >> {:.15f}'.format(time_end))
        return res
    return wrapper


def get_exponentiation(numbers=[], **params):
    '''
        Фунцкия для возведения целых числе в степень.
        Функция принимает список целых чисел, а так же дополнительно аргумент exp в котором хранится в какую степено необходимо возвести все числа.
        Данная функция ожидает, что пользователь будет вводить только корректные значения, поэтому не делает лишних проверок.
    '''
    result, e = [], 2
    if 'exp' in params:
        e = params['exp']
    for i in numbers:
        result.append(i ** e)
    return result


def is_prime(num):
    '''
        Функция для определения простое число было получено на вход или нет.
    '''
    count = 0
    for i in range(num):
        if not num % (i+1):
            count += 1
    if count < 3:
        return True
    else:
        return False


@lead_time
def get_number_by_type(numbers=[], **params):
    '''
        Функция для поиска и вывода четных/нечетных/простых чисел из переданного списка целых чисел.
        Функция принимает список из целых числе, а так же дополнительно аргумент num_type, который указывает какого типа числа нам необходимо найти в списке. По умолчанию, функци выводит только четные числа, хотя можно было вывести сообщение пользователю, что параметр выбора типа обязательный дописав после if секцию else print(err) return [].
        Данная функция ожидает, что пользователь будет вводить только корректные значения, поэтому не делает лишних проверок.

        Так как, в функции присутствует довольно тупой способ поиска простынх чисел, поэтому было принято решение повесить на неё декоратор, который будет показывать врем выполнения функции. Когда данное значение выйдет за рамки допустимого, можно будет озадачиться написанием более быстрой функци для посика простых числе.
    '''
    dict_types = {'even': 0, 'odd': 1, 'prime': 2}
    result, my_type = [], dict_types['even']
    if 'num_type' in params:
        my_type = dict_types[params['num_type']] or dict_types['even']
    for num in numbers:
        if my_type == 0 and not(num % 2):
            result.append(num)
        elif my_type == 1 and (num % 2):
            result.append(num)
        elif my_type == 2 and ((num % 2) or num == 2):
            if is_prime(num):
                result.append(num)
    return result


def in_func(func):
    '''
        Декоратор для отображения вложенности рекурсии
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if '__count' in kwargs:
            kwargs['__count'] += 1
        else:
            kwargs['__count'] = 0
        print('____' * kwargs['__count'], '--> {}{}'.format(func.__name__, args))
        res = func(*args, **kwargs)
        print('____' * kwargs['__count'], '<-- {}{} == {}'.format(func.__name__, args, res))
        return res
    return wrapper


@in_func
def fib(num, **kwargs):
    '''
        Функция для вычисления числа Фибоначи через рекурсивный обход
    '''
    if num == 1:
        return 1
    elif num == 0:
        return 0
    return fib(num - 1, **kwargs) + fib(num - 2, **kwargs)


'''
    По желанию ревьевера, весь main был обёрнут в if
'''
if __name__ == '__main__':
    '''
        Исходные данные. Будем использовать их в обоих примерах.
    '''
    my_numbers = [1, 2, 3, 4, 5, 6, 9, 10, 17, 22]
    print('Source numbers:', my_numbers)
    print('')

    '''
        Вывод результата функции по возведению в степень.
    '''
    print('get_exponentiation()')
    print('Numbers to 2:', get_exponentiation(my_numbers))
    print('Numbers to 3:', get_exponentiation(my_numbers, exp=3))
    print('')

    '''
        Вывод результата функции по поиску чисел с выбранным типом.
    '''
    print('get_number_by_type()')
    print('Even numbers:',  get_number_by_type(my_numbers))
    print('Odd numbers:',   get_number_by_type(my_numbers, num_type='odd'))
    print('Prime numbers:', get_number_by_type(my_numbers, num_type='prime'))
    print('')

    '''
        Вывод результата по вычислению числа Фибоначи
    '''
    print('fib()')
    for i in (3, 5):
        res = fib(i)
        print('{}th elem in the Fibonacci series: {}'.format(i, res))
