import sys


def main():
    data = sys.stdin.readline().strip()
    s = data.strip()
    print(min_crossings(s))


def min_crossings(s: str) -> int:
    left = 0        
    right = 1
    for i in s:
        if i == 'L':
            new_left = min(left + 1, right + 2) 
            new_right = min(right, left + 1)      
        elif i == 'R':
            new_left = min(left, right + 1)
            new_right = min(right + 1, left + 2)
        else:
            new_left = min(left + 1, right + 2)
            new_right = min(right + 1, left + 2)
        left, right = new_left, new_right
    return min(right, left + 1)


if __name__ == "__main__":
    main()