import sys
from collections import Counter


def main():
    
    s = sys.stdin.readline().strip()
    arr = list(s)
    
    n = len(arr)

    main_sum = n * (n - 1) // 2
    
    a = Counter(arr)

    for i in a:
        count = a[i]
        main_sum -= count * (count - 1) // 2

    print(main_sum + 1)

if __name__ == '__main__':
    main()
