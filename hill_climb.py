import sys

import numpy as np

from bin_vec import BinVec


def target_fn(bin_vec: BinVec, values: list[int], mat: np.array) -> int:
    if not vec_is_fine(bin_vec, mat):
        return sys.maxsize
    return sum(bin_vec.bits * values)


def vec_is_fine(bin_vec: BinVec, mat: np.array) -> bool:
    stacked = np.zeros(mat.shape[:1], dtype=int)
    for j in range(len(bin_vec.bits)):
        if bin_vec.bits[j] == 0:
            continue
        stacked += mat.T[j]
    return (stacked == np.ones_like(stacked)).all()


def hill_climb_min(values: list[int], mat: np.array) -> BinVec:
    x = BinVec.random(len(values))
    while True:
        minimum = sys.maxsize
        y = x.clone()
        for each in x.two_flip():
            temp = target_fn(each, values, mat)
            if temp < minimum:
                minimum = temp
                y = each
        if target_fn(y, values, mat) < target_fn(x, values, mat):
            x = y
        else:
            break
    return x
