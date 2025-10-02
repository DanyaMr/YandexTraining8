import sys


def main():
    sum = 0
    i, k = map(int, sys.stdin.readline().strip().split())
    if i % 10 == 0:
        None
    elif i % 10 == 5:
        i += 5
    elif k > 4:
        while i % 10 != 2:
            i += i % 10
            k -= 1

        if k > 4:
            i += (k // 4) * 20
        else:
            for _ in range(k):
                if i % 10 == 0:
                    break
                i += i % 10

        for _ in range(k - (k // 4) * 4):
            i += i % 10
    else:
        for _ in range(k):
            if i % 10 == 0:
                break
            i += i % 10

    print(i)

if __name__ == '__main__':
    main()
