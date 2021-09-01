from typing import List


def weird_algorithm(n: int) -> List[int]:
    res = [
        n,
    ]
    while n != 1:
        if n & 1:
            n = n * 3 + 1
            res.append(n)
        else:
            n = n // 2
            res.append(n)

    return res


if __name__ == "__main__":
    n = int(input())
    for i in weird_algorithm(n):
        print(i, end=" ")
