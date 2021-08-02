import time

class FiboIter():

    def __init__(self, max=None) -> None:
        self.max = max


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if not self.max or self.n1 + self.n2 <= self.max:
                #self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.n1 + self.n2
                self.counter += 1
                return self.n2
            else:
                raise StopIteration

if __name__ == "__main__":
    limit = input("What is tha maximum you want to apply?\n")
    try:
        limit = int(limit)
    except:
        print("Please insert a number")
        exit()

    fibonacci = FiboIter(max=limit)

    for element in fibonacci:
        print(element)
        time.sleep(0.05)
