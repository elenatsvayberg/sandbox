class Test(object):
    def __init__(self, word, num):
        self.word = word
        self.num = num
    def __str__ (self):
        return "Values in this object:\
               word = {word}, num = {num}".format(word = self.word, num = self.num)

a = Test(word = "Hello", num =5)
print(a)


class Test2(object):
    def __init__(self, text, num):
        self.text = text
        self.num = num
    def __str__ (self):
        print("NO")

t = Test(text = "Hi", num =5)
print(t)
