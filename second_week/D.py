import sys


def main():
    words_set = set()

    sentence = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        words_set.add(sys.stdin.readline().strip())

    separate(sentence, words_set, n)

def separate(sentence: str, words_set: set, n: int):
    arr = [-1] * (len(sentence) + 1)
    arr[0] = 0  
    
    for i in range(1, len(sentence) + 1):
        for j in range(i):
            if arr[j] != -1 and sentence[j:i] in words_set:
                arr[i] = j
                break
    
    res = []
    i = len(sentence)
    while i > 0:
        start = arr[i]
        res.append(sentence[start:i])
        i = start
    res.reverse()
    
    print(' '.join(res))

if __name__ == '__main__':
    main()

    