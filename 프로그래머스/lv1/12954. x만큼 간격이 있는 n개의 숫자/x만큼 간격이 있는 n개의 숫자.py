def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return [x*i for i in range(1,n+1)]