class OddNumbers:

    def __init__(self, numbers_to_return):
        self.start = 1
        self.count = 0
        self.numbers_to_return = numbers_to_return

    def __iter__(self):
        return self

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.numbers_to_return:
            self.count += 1
            temp = self.start
            self.start += 2
            return temp
        else:
            raise StopIteration


my_iter = OddNumbers(5)

while True:
    try:
        nextEle = next(my_iter)
        print(nextEle)
    except StopIteration:
        break