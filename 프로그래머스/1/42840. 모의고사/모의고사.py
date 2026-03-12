def solution(answers):
    answer = []

    one = [1, 2, 3, 4, 5] * len(answers)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers)
    scores = [0, 0, 0]

    for i in range(len(answers)):
        if one[i] == answers[i]:
            scores[0] += 1
        if two[i] == answers[i]:
            scores[1] += 1
        if three[i] == answers[i]:
            scores[2] += 1
            
    for i in range(3):
        if max(scores) == scores[i]:
            answer.append(i + 1)
    
    return answer