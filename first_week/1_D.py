import sys
from collections import Counter

def main():
    
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    frequency = Counter(arr)

    res = ""

    count = 0
    for i in frequency:
        if k == count:
            break
        res += str(i) + " "
        count += 1

    if count < k:   
        for i in frequency:
            while frequency[i] > 1 and count < k:
                frequency[i] -= 1
                count += 1
                res += str(i) + " "
    print(res)
    
if __name__ == '__main__':
    main()
