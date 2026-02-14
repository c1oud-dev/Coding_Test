def solution(box, n):
    # 각 방향별로 들어갈 수 있는 주사위 개수를 구해서 곱합니다.
    width = box[0] // n
    length = box[1] // n
    height = box[2] // n
    
    return width * length * height