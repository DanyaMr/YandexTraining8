import sys


def main():
    n = int(sys.stdin.readline
            ().strip())
    s = sys.stdin.readline().strip()
    nums = list(map(int, s.split()))
    arr1 = nums[::2] 
    arr2 = nums[1::2]

    sum1 = sum(arr1)
    sum2 = sum(arr2)
    min1 = min(arr1)
    max2 = max(arr2)
    
    if min1 < max2:
        sum1 += (max2 - min1)
        sum2 += (min1 - max2)
    print(sum1 - sum2)

if __name__ == '__main__':
    main()




