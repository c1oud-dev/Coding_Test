'''
pi-1, pi, pi+1 중 pi가 최솟값도, 최댓값도 아니라면 pi는 평범한 숫자이다.
평범한 숫자의 개수를 출력
'''
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = 0

    for i in range(1, N - 1):  # 1, 2, 3
        if sorted([nums[i - 1], nums[i], nums[i + 1]])[1] == nums[i]:
            result += 1
    print(f"#{test_case} {result}")