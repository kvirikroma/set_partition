import sys
from bin_vec import BinVec
from numpy import matrix


def target_fn(bin_vec: BinVec, values: list[int], matrix: matrix) -> int:
    if not vec_is_fine(bin_vec, matrix):
        return sys.maxsize

    sum = 0
    for i in range(len(bin_vec.bits)):
        sum += bin_vec.bits[i] * values[i]

    return sum


def vec_is_fine(bin_vec: BinVec, mat: matrix) -> bool:
    n = len(bin_vec.bits)
    stacked = [0 for _ in range(mat.shape[0])]

    for j in range(len(bin_vec.bits)):
        if bin_vec.bits[j] == 0:
            continue

        col = mat[:, j].getA1()
        for i in range(len(col)):
            stacked[i] += col[i]

    for e in stacked:
        if e != 1:
            return False

    return True


def hill_climb_min(values: list[int], mat: matrix) -> BinVec:
    x = BinVec.random(len(values))
    found = True

    while found:
        min = sys.maxsize
        y = x.clone()

        for each in x.two_flip():
            temp = target_fn(each, values, mat)
            if temp < min:
                min = temp
                y = each

        if target_fn(y, values, mat) < target_fn(x, values, mat):
            x = y
        else:
            found = False

    return x
