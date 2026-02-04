def solution(array):
    return sorted(array)[len(array)//2]

# 정렬 함수 sort() vs sorted()
# list.sort() - 다른 리스트에 안 담아도 됨(원본 변경)
# sorted(list) - 다른 리스트에 담김(원본 유지)