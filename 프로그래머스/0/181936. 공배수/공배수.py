def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0

# bool() 사용 가능
# int(bool(number % n == 0) & bool(number % m == 0))