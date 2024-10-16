import decimal

# 고정 소수점의 소수점 자리수 설정
decimal.getcontext().prec = 28  # 원하는 자릿수로 설정 (예: 28자리)

a = decimal.Decimal(0)
for i in range(100000000000):
    term = decimal.Decimal((-1) ** i) * (decimal.Decimal(4) / (decimal.Decimal(2 * i + 1)))
    a += term
    print(a)
