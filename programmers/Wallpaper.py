def solution(wallpaper):
    answer = []
    X=[]
    Y=[]
    for i in range(len(wallpaper)): # 행 
        for j,v in enumerate(wallpaper[i]): # 열
            if v=='#':
                X.append(i)
                Y.append(j)
    answer=[min(X),min(Y),max(X)+1,max(Y)+1]
    
    return answer

## https://school.programmers.co.kr/learn/courses/30/lessons/161990

    
