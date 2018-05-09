class Test(object):
    def __init__(self, num):
        self.num = num

    def __eg__(self, other):
        if self.num == self.other:
            return True
        else:
            return False


a = Test(5)
b = Test(5)
c = Test(4)
print(a == b)
print(a == c)

print(a, b, c)

