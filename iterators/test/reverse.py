class Reverse:
    def __init__(self, ls):
        self.ls = ls
        self.index = len(ls) - 1

    def __iter__(self):
        return self.ls[self.index]

    def __next__(self):
        self.index -= 1
        return self.ls[self.index]
