import sys


def main():

    n, m = map(int, sys.stdin.readline().strip().split())

    arr = list()

    for _ in range(n):
        s = list(sys.stdin.readline().strip())
        arr.append(s)

    print(counting(arr, n, m))

def counting(arr, n, m) -> str:
    counter = 1
    for i in range(n):
        for j in range(m):
            if m > j + 4:
                if arr[i][j + 4] == arr[i][j] and arr[i][j] != '.':
                    for x in range(1, 4):
                        if arr[i][j] == arr[i][j + x]:
                            counter += 1
                    if counter == 4:
                        return "Yes"
            counter = 1
            if n > i + 4:
                if arr[i + 4][j] == arr[i][j] and arr[i][j] != '.':
                    for x in range(1, 4):
                        if arr[i][j] == arr[i + x][j]:
                            counter += 1
                    if counter == 4:
                        return "Yes"
            counter = 1
            if n > i + 4 and m > j + 4:
                if arr[i + 4][j + 4] == arr[i][j] and arr[i][j] != '.':
                    for x in range(1, 4):
                        if arr[i][j] == arr[i + x][j + x]:
                            counter += 1
                    if counter == 4:
                        return "Yes"
            counter = 1
            if n > i + 4 and j - 4 >= 0:
                if arr[i + 4][j - 4] == arr[i][j] and arr[i][j] != '.':
                    for x in range(1, 4):
                        if arr[i][j] == arr[i + x][j - x]:
                            counter += 1
                    if counter == 4:
                        return "Yes"
            counter = 1
    return "No"
                 

if __name__ == '__main__':
    main()
