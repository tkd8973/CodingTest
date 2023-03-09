def solution(num, total):
    answer=[]
    print(num//2)
    if num%2==1:
        return [(total//num)+i for i in range((-num+1)//2,(num+1)//2)]
    else:
        return [(total//num)+i+1 for i in range((-num+1)//2,(num+1)//2)]