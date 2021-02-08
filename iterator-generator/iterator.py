class PowThree:
    """
    Class to implement an interator
    of powers of three
    """

    def __init__(self, max = 0):
        self.max = max
    
    def __iter__(self):
        self.to_n = 0
        return self
    
    def __next__(self):
        if self.to_n <= self.max:
            result = 3 ** self.to_n
            self.to_n +=1
            return result
        else:
            raise StopIteration


if __name__ == "__main__":

    numbers = PowThree(5)

    iterObject = iter(numbers)

    # Using next to get to the next iterator element
    print(next(iterObject))
    print(next(iterObject))
    print(next(iterObject))
    print(next(iterObject))
    print(next(iterObject))