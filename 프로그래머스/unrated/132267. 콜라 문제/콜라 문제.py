def solution(a, b, n):
    answer=0
    for i in range(n):
        div = (n//a)*b
        mod = n%a
        print(div,mod)
        n=div+mod
        answer+=div
        
        if n<a:
            break
    return answer