def solution(score):
    totals = [sum(s) for s in score]
    sorted_totals = sorted(totals, reverse=True)
    return [sorted_totals.index(t) + 1 for t in totals]