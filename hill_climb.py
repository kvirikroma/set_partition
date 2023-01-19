import sys

import numpy as np

from bin_vec import BinVec


def target_fn(bin_vec: BinVec, values: list[int], mat: np.matrix) -> int:
    if not vec_is_fine(bin_vec, mat):
        return sys.maxsize
    result = 0
    for i in range(len(bin_vec.bits)):
        result += bin_vec.bits[i] * values[i]
    return result


def vec_is_fine(bin_vec: BinVec, mat: np.matrix) -> bool:
    stacked = np.zeros(mat.shape[:1], dtype=int)
    for j in range(len(bin_vec.bits)):
        if bin_vec.bits[j] == 0:
            continue
        col = mat[:, j].getA1()
        stacked += col
    return (stacked == np.ones_like(stacked)).all()


def hill_climb_min(values: list[int], mat: np.matrix) -> BinVec:
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
