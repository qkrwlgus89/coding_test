# 한 번 계산된 결과를 메모이제이션하기 위한 리스트
d = [0] * 100

# 피보나치 함수 (탑다운 DP)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

n = int(input())
print(fibo(n))