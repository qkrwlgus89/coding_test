S = int(input())

sum_val = 0
n = 0

while True:
    n += 1
    sum_val += n
    if sum_val > S:
        print(n - 1)
        break