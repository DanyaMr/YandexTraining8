import sys


def main():
    arr = list()

    n = int(sys.stdin.readline().strip())

    if n != 0:
        for i in range(n):
            s = list(map(float, sys.stdin.readline().strip().split()))
            arr.append(s)
        
        for i in range(len(arr)):
            arr[i].append((arr[i][2] / abs(arr[i][1] - arr[i][0])) )
        
        sorted_arr = sorted(arr, key=lambda x: x[3], reverse=True)

        max_sum = sorted_arr[i][2]
        for i in range(n):
            uniq_set = list()
            sum = sorted_arr[i][2]
            uniq_set.append(sorted_arr[i])
            for j in range(n):
                count = 0
                x = (sorted_arr[j][1] + sorted_arr[j][0]) / 2
                for l in range(len(uniq_set)):
                    y = (uniq_set[l][1] + uniq_set[l][0]) / 2 

                    if not (sorted_arr[j][0] <= y <= sorted_arr[j][1]) and \
                        not (uniq_set[l][0] <= x <= uniq_set[l][1]) and \
                         not (sorted_arr[j][1] > uniq_set[l][0] and sorted_arr[j][0] < uniq_set[l][0]) and \
                          not (sorted_arr[j][0] < uniq_set[l][1] and sorted_arr[j][1] > uniq_set[l][1]):
                        count += 1
                if count == len(uniq_set):
                    uniq_set.append(sorted_arr[j])
                    sum += sorted_arr[j][2]
                if sum > max_sum:
                    max_sum = sum

        print(max_sum)
    else:
        print(0)     
        
    
    

if __name__ == '__main__':
    main()

