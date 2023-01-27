import numpy as np


class BinVec:
    def __init__(self, bits: np.array):
        self.bits = bits

    @staticmethod
    def random(length: int):
        return BinVec(np.random.randint(2, size=length))

    @staticmethod
    def ones(length: int):
        return BinVec(np.ones((length,), dtype=int))

    def one_flip(self):
        flips = [self.clone()]
        for i in range(len(self.bits)):
            copy = self.clone()
            copy.bits[i] = 1 - copy.bits[i]
            flips.append(copy)
        return flips

    def two_flip(self):
        yield self.clone()
        for i in range(len(self.bits)):
            for j in range(i, len(self.bits)):
                copy = self.clone()
                copy.bits[i] = 1 - copy.bits[i]
                if i != j:
                    copy.bits[j] = 1 - copy.bits[j]
                yield copy

    def three_flip(self):
        yield self.clone()
        for i in range(len(self.bits)):
            for j in range(i, len(self.bits)):
                for k in range(j, len(self.bits)):
                    copy = self.clone()
                    copy.bits[i] = 1 - copy.bits[i]
                    if i != j:
                        copy.bits[j] = 1 - copy.bits[j]
                    if k != i and k != j:
                        copy.bits[k] = 1 - copy.bits[k]
                    yield copy

    def clone(self):
        return BinVec(self.bits.copy())
