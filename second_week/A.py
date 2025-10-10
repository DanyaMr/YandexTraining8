import sys
from functools import lru_cache

def main():
    s = int(sys.stdin.readline().strip())

    print(count(s))

@lru_cache(maxsize=None)
def count(remained: int) -> int:
    if remained == 0:
        return 1
    if remained < 0:
        return 0
    return count(remained - 1) + count(remained - 2) + count(remained - 3)

if __name__ == '__main__':
    main()
