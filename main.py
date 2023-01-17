import sys
from typing import Tuple
from bin_vec import BinVec
from numpy import matrix, zeros
from hill_climb import hill_climb_min, target_fn


def read_file(path: str) -> Tuple[list[int], matrix]:
    file = open(path)
    lines = list(map(lambda l: l.strip(), file.readlines()))

    shape = list(filter(lambda e: e != "", lines[0].split(" ")))
    mat = zeros((int(shape[0]), int(shape[1])), dtype=int)
    values = []

    for i in range(1, len(lines)):
        nums = list(filter(lambda e: e != "", lines[i].split(" ")))
        values.append(int(nums[0]))

        for j in nums[2:]:
            mat[int(j) - 1, i - 1] = 1

    return (values, matrix(mat))


def run(runs: int, values: list[int], mat: matrix):
    results = []
    for i in range(0, runs):
        vec = hill_climb_min(values, mat)
        target_fn_val = target_fn(vec, values, mat)
        results.append(target_fn_val)
        print(f"Run {i + 1}: {target_fn_val}")

    return results


def analyze(results: list[int], values: list[int], mat: matrix):
    best = (sys.maxsize, 0)
    worst = (0, 0)

    for i in range(len(results)):
        res = results[i]
        if res == sys.maxsize:
            continue

        if res < best[0]:
            best = (res, i + 1)
        if res > worst[0]:
            worst = (res, i + 1)

    print(f"\nBest: {best[1]} - {best[0]}\nWorst: {worst[1]} - {worst[0]}")

    max_fn = target_fn(BinVec.ones(len(values)), values, mat)
    base = max_fn - worst[0]
    print(f"Diff: {(max_fn - best[0] - base) / base * 100} %")


def main():
    (values, mat) = read_file("data/test.txt")

    # Debug print
    # print(f"{values}\n{mat}\n")

    results = run(100, values, mat)
    analyze(results, values, mat)


if __name__ == "__main__":
    main()
