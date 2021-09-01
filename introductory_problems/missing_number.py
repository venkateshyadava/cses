from typing import List


def missing_number(n: int, l: List) -> int:
    return ((n * (n + 1)) // 2) - sum(l)


if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().split()))
    print(missing_number(n, l))