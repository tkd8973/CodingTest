def solution(keymap, targets):
    answer = []
    result = 0
    dic=dict()
    index=[]
    for i in keymap:
        for j,v in enumerate(i):
            if v in dic.keys():
                dic[v]=min(j+1,dic[v])
            else:
                dic[v]=j+1
                
    for i in targets:
        for j,v in enumerate(i):
            try:
                result = result+dic[v]
            except:
                result=-1
                break
        answer.append(result)
        result=0
            
    return answer
