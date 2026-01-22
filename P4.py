from sys import stdin
import sys
sys.setrecursionlimit(20000)

def calculate_effective_volume(n, S1, S2):
    it1 = iter(S1)
    it2 = iter(S2)
    def skip(it):
        c = next(it)
        if c == '2':
            for _ in range(8):
                skip(it)
    def getvol(it, size):
        c = next(it)
        if c == '0':
            return 0
        elif c == '1':
            return size ** 3
        else:
            sub_size = size // 2
            total = 0
            for _ in range(8):
                total += getvol(it, sub_size)
            return total
    def solve(size):
        c1 = next(it1)
        c2 = next(it2)

        if c1 == '2' and c2 == '2':
            sub_size = size // 2
            total = 0
            for _ in range(8):
                total += solve(sub_size)
            return total

        elif c1 == '0' or c2 == '0':
            if c1 == '2':
                for _ in range(8): skip(it1)
            if c2 == '2':
                for _ in range(8): skip(it2)
            return 0

        elif c1 == '1' and c2 == '1':
            return size ** 3

        elif c1 == '1' and c2 == '2':
            sub_size = size // 2
            total = 0
            for _ in range(8):
                total += getvol(it2, sub_size)
            return total

        elif c1 == '2' and c2 == '1':
            sub_size = size // 2
            total = 0
            for _ in range(8):
                total += getvol(it1, sub_size)
            return total
        return 0
    return solve(n)
n = int(stdin.readline().strip())
S1 = stdin.readline().strip()
S2 = stdin.readline().strip()
print(calculate_effective_volume(n, S1, S2))