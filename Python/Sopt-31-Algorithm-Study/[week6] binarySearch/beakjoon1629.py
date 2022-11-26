
# 분할 정복
def dac(a, b, c):
  if b == 1:
    return a % c
    
  if b % 2 == 0:
    return dac(a, b//2, c) ** 2
  else:
    return (dac(a, b//2, c) ** 2) * a


# 입력 값
a, b, c = map(int, input().split())

# 결과 값
print(dac(a, b, c))
