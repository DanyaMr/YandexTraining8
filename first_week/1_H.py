import sys


def main():

    n, m = map(int, sys.stdin.readline().strip().split())
    source = sys.stdin.readline().strip()

    arr = list()
    s = dict()

    k = n // m

    for _ in range(m):
        x = sys.stdin.readline().strip()
        arr.append(x)

    for x in arr:
        if x in s:
            s[x] += 1
        else:
            s[x] = 1

    res = list()
    counter = 0
    for _ in range(m):
        subline = source[counter:counter + k]
        if s[subline] > 0:
            s[subline] -= 1
        index = arr.index(subline) + 1
        res.append(index)
        arr[index - 1] = ""
        
        counter += k

    print(" ".join(map(str, res)))


if __name__ == '__main__':
    main()
