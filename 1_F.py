import sys


def main():

    n, m = map(int, sys.stdin.readline().strip().split())

    arr = list()

    for i in range(n):
        s = list(sys.stdin.readline().strip())
        arr.append(s)

    max, control_max_j = find_max_row(arr, n, m)
    min, control_min_i = find_min_column(arr, n, m)

    if arr[control_min_i][control_max_j] == '?':
        max -= 2

    print(max - min)

def find_max_row(arr, n, m):
    max_sum = 0
    counter_plus = 0
    counter_minus = 0
    counter_question = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == '+':
                counter_plus += 1
            elif arr[i][j] == '-':
                counter_minus += 1
            else:
                counter_question += 1

        current_sum = counter_plus + counter_question - counter_minus
        if current_sum > max_sum:
            
            cotrol_question = counter_question
            max_sum = current_sum
            control_j = j
        counter_plus = 0
        counter_minus = 0
        counter_question = 0

    return max_sum, control_j


def find_min_column(arr, n, m):
    min_sum = 0
    counter_plus = 0
    counter_minus = 0
    counter_question = 0

    for i in range(m):
        for j in range(n):
            if arr[j][i] == '+':
                counter_plus += 1
            elif arr[j][i] == '-':
                counter_minus += 1
            else:
                counter_question += 1

        current_sum = counter_plus - counter_question - counter_minus
        if current_sum < min_sum:
            min_sum = current_sum
            control_i = j
        counter_plus = 0
        counter_minus = 0
        counter_question = 0

    return min_sum, control_i


if __name__ == '__main__':
    main()
