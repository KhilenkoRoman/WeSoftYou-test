# Все ли верно в этом участке кода?
class A:
    attr1 = 1

    def set_some_value(self, value):
        self.attr2 = value

a = A()
a.set_some_value(1)
print(a.attr2)