def solution(ingredient):
    answer = 0
    s=[]
    prd = [1,2,3,1]
    for i in ingredient:
        s.append(i)
        if s[-4:] == prd:
            answer+=1
            del s[-4:]
            
        
    return answer