'''
1. Можем ли мы отнаследовать новый класс С и от класса А и от В одновременно?
2. Что выведет последняя строка и почему? 
'''
class A:
    attr1 =1
    attr2 =1

class B:
    attr2= 2

class C(A, B):
    attr3=3

class D(C):
    attr4 = 4

a = D()
print(a.attr2)