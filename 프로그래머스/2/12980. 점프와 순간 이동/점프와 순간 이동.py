def solution(n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
            n -= 1  # jump
            ans += 1
        n //= 2

    return ans