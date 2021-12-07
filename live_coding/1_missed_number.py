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