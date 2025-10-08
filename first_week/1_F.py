# import sys


# def main():

#     n, m = map(int, sys.stdin.readline().strip().split())

#     arr = list()

#     for i in range(n):
#         s = list(sys.stdin.readline().strip())
#         arr.append(s)



#     max, control_max_i = find_max_row(arr, n, m)
#     min, control_min_j = find_min_column(arr, n, m, control_max_i)

#     if arr[control_max_i][control_min_j] == '?':
#         max -= 2

#     print(max - min)

# def find_start_max_sum(arr, n, m):
#     counter_minus = 0
#     counter_plus = 0
#     counter_question = 0
#     for i in range(1):
#         for j in range(m):
#             if arr[i][j] == '+':
#                 counter_plus += 1
#             elif arr[i][j] == '-':
#                 counter_minus += 1
#             else:
#                 counter_question += 1

#         current_sum = counter_plus + counter_question - counter_minus
#         max_sum = current_sum
#         control_j = i
#         conrtol_question = counter_question

#     return max_sum, control_j, conrtol_question

# def find_start_min_sum(arr, n, m):
#     counter_minus = 0
#     counter_plus = 0
#     counter_question = 0
#     for i in range(1):
#         for j in range(n):
#             if arr[j][i] == '+':
#                 counter_plus += 1
#             elif arr[j][i] == '-':
#                 counter_minus += 1
#             else:
#                 counter_question += 1

#         current_sum = counter_plus - counter_question - counter_minus
#         min_sum = current_sum
#         control_j = i

#     return min_sum, control_j

# def find_max_row(arr, n, m):
#     max_sum, control_j, control_question = find_start_max_sum(arr, n, m)
#     counter_plus = 0
#     counter_minus = 0
#     counter_question = 0

#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == '+':
#                 counter_plus += 1
#             elif arr[i][j] == '-':
#                 counter_minus += 1
#             else:
#                 counter_question += 1

#         current_sum = counter_plus + counter_question - counter_minus
        
#         if current_sum >= max_sum:
#             if counter_question and current_sum == max_sum and counter_question < control_question:
#                 control_question = counter_question
#                 control_j = i
#             elif current_sum > max_sum:
#                 control_question = counter_question
#                 max_sum = current_sum
#                 control_j = i
#         counter_plus = 0
#         counter_minus = 0
#         counter_question = 0

#     return max_sum, control_j


# def find_min_column(arr, n, m, l):
#     min_sum, control_j = find_start_min_sum(arr, n, m)
#     counter_plus = 0
#     counter_minus = 0
#     counter_question = 0

#     for i in range(m):
#         for j in range(n):
#             if arr[j][i] == '+':
#                 counter_plus += 1
#             elif arr[j][i] == '-':
#                 counter_minus += 1
#             else:
#                 counter_question += 1

#         current_sum = counter_plus - counter_question - counter_minus
#         if current_sum <= min_sum:
#             if arr[l][i] != '?' and current_sum == min_sum:
#                 min_sum = current_sum
#                 control_j = i
#             elif current_sum < min_sum:
#                 min_sum = current_sum
#                 control_j = i

#         counter_plus = 0
#         counter_minus = 0
#         counter_question = 0

#     return min_sum, control_j


# if __name__ == '__main__':
#     main()

import sys


def main():

    n, m = map(int, sys.stdin.readline().strip().split())

    arr = list()

    for i in range(n):
        s = list(sys.stdin.readline().strip())
        arr.append(s)

    print(find_max_in_list(arr, n, m))
    

def arr_sum_rows(arr, n, m):

    arr_rows = list()
    counter_minus = 0
    counter_plus = 0
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
        counter_minus = 0
        counter_plus = 0
        counter_question = 0
        arr_rows.append(current_sum)

    return arr_rows

def arr_sum_columns(arr, n, m):
    
    arr_columns = list()
    counter_minus = 0
    counter_plus = 0
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
        counter_minus = 0
        counter_plus = 0
        counter_question = 0
        arr_columns.append(current_sum)

    return arr_columns

def find_max(arr, n, m):
    arr_rows = arr_sum_rows(arr, n, m)
    arr_columns = arr_sum_columns(arr, n, m)
    res = [[] for _ in range(n)]
    for i in range(len(arr_rows)):
        for j in range(len(arr_columns)):
            if arr[i][j] == '?':
                res[i].append(arr_rows[i] - 2 - arr_columns[j])
            else:
                res[i].append(arr_rows[i] - arr_columns[j])
    return res

def find_max_in_list(arr, n, m):
    res = find_max(arr, n, m)
    max = res[0][0]
    for i in range(n):
        for j in range(m):
            if res[i][j] >= max:
                max = res[i][j]
    return max

if __name__ == '__main__':
    main()
