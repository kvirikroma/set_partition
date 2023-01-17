import random


class BinVec:
    def __init__(self, bits: list[int]):
        self.bits = bits

    def random(len: int):
        return BinVec([random.randint(0, 1) for _ in range(len)])

    def ones(len: int):
        return BinVec([1 for _ in range(len)])

    def one_flip(self):
        flips = [self.clone()]
        for i in range(len(self.bits)):
            copy = self.clone()
            copy.bits[i] = 1 - copy.bits[i]
            flips.append(copy)
        return flips

    def two_flip(self):
        flips = [self.clone()]
        for i in range(len(self.bits)):
            for j in range(i, len(self.bits)):
                copy = self.clone()
                copy.bits[i] = 1 - copy.bits[i]

                if i != j:
                    copy.bits[j] = 1 - copy.bits[j]

                flips.append(copy)
        return flips

    def clone(self):
        return BinVec(self.bits[:])
