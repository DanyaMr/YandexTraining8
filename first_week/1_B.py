from decimal import Decimal, ROUND_HALF_UP, getcontext
import sys

def main():

    getcontext().prec = 30

    s = sys.stdin.readline().strip()

    a, b, c, v0, v1, v2 = map(Decimal, s.split())
    minimum = []

    sum11 = a / v0 + c / v1 + c / v2 + a / v2
    sum12 = a / v0 + c / v0 + c / v1 + a / v2
    sum2 = a / v0 + a / v1 + b / v0 + b / v1
    sum2_1 = a / v0 + c / v1 + b / v2
    sum2_2 = a / v0 + a / v1 + b / v0 + b / v1
    sum5_1 = a / v0 + a / v1 + a / v0 + c / v0 + c / v1 + a / v1
    minimum.extend([sum11, sum12, sum2, sum2_1, sum2_2, sum2_2, sum5_1])

    sum11 = b / v0 + c / v1 + c / v2 + b / v2
    sum12 = b / v0 + c / v0 + c / v1 + b / v2
    sum2 = b / v0 + b / v1 + a / v0 + a / v1
    sum2_1 = b / v0 + c / v1 + a / v2
    sum2_2 = b / v0 + b / v1 + a / v0 + a / v1
    sum5_1 = b / v0 + b / v1 + b / v0 + c / v0 + c / v1 + b / v1
    minimum.extend([sum11, sum12, sum2, sum2_1, sum2_2, sum2_2, sum5_1])
    
    x = min(minimum)
    x = x.quantize(Decimal('0.000000000000001'), rounding=ROUND_HALF_UP)
    print(x)

if __name__ == '__main__':
    main()


