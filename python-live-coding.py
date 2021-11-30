# =============================================================================
'''
Missed number

a = [1, 3, 2 ... N]:
    - a contains numbers from 1 to 100
    - one number is missed
    - a is unsorted
    ? Find the missed number
'''
import random


def get_unsorted_list_with_missed_number():
    list1 = [item for item in range(1, 101)]
    random.shuffle(list1)
    del list1[0]
    return list1

a = get_unsorted_list_with_missed_number()

# # Write your code below
# b = [item for item in range(1, 101)]
# print(set(b) - set(a))


# =============================================================================
'''
1. Можем ли мы отнаследовать новый класс С и от класса А и от В одновременно?
2. Что выведет последняя строка и почему? 
'''
class A:
    attr1 =1
    attr2 =1

class B:
    attr2= 2

# -------------------------
class C(A, B):
    attr3=3

class D(C):
    attr4 = 4

a = D()
print(a.attr2)
# =============================================================================
'''
Как можно поменять местами ключи и значения в словаре?
'''
degrees = {i: i*i for i in range(1, 10)}

#-------------------
# degrees = dict(zip(degrees.values(), degrees.keys()))

# =============================================================================
'''
Как можно объединить все элеименты списка в строку, через запятую?
'''
import string

alphabet = [i for i in string.ascii_lowercase]

#-------------------
print(', '.join(alphabet))
# =============================================================================
'''
Как можно подсчитать количество вхождений каждой буквы?
'''
glossolalia = 'абабагаламага'

#-------------------
# from collections import Counter
# letter_counter = Counter(list(glossolalia))


# =============================================================================

# Все ли верно в этом участке кода?
class A:
    attr1 = 1

    def set_some_value(self, value):
        self.attr2 = value

a = A()
a.set_some_value(1)
print(a.attr2)