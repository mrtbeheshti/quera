class Reverse:
    def __init__(self, ls):
        self.ls = ls
        self.index = len(ls) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            result = self.ls[self.index]
            self.index -= 1
            return result
        raise StopIteration


ls = [10, 20, 30]
for it in Reverse(ls):
    print(it)
print(ls)
