N, M = map(int, input().split())
ans_list = []
visited=[False]*N   # [1,2,3,4]에서 사용했는지 안했는지 여부


def combination(count):             # count는 자릿수
    if(count ==M):                  # M자리 숫자가 만들어지면 수행
        answer = " ".join(map(str,ans_list))    #리스트를 문자열로 변환하여 출력
        print(answer)
        return

    for i in range(1,N+1):          # [1,2,3,4]
        if(visited[i-1]==False):    # false, 사용안한 i 일때,
            ans_list.append(i)      # i =1을 삽입
            visited[i-1]=True       # i =1을 사용했다 표기
            combination(count+1)    # 위의 3줄과 같은방식으로 다음 자식layer들 모두 진행
            visited[i-1]=False      # 첫칸에 새로운 i를 삽입시키기위해, 사용안함으로 체크 후
            ans_list.remove(i)      # 지워주기

combination(0)
