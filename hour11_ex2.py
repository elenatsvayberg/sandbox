class Test(object):
    def __init__(self, num):
        self.num = num
    def __eg__(self,other):
        self.other == self.num
        return True
    def __ne__(self, other):
        if self.num != other.num:
            return True
        else:
            return False
a = Test(5)
b = Test(5)
c = Test(7)


print(a != b)
print(c != b)

class Test(object):
    def __init__(self, num):
        self.num=num
    def __gte__(self, other):
        if self.num >= other.num:
             return True
        else:
            return False

alfa = Test(5)
beta = Test(5)
gamma = Test(6)

print(alfa >= beta)

print(alfa >= gamma)

print(gamma >= alfa)