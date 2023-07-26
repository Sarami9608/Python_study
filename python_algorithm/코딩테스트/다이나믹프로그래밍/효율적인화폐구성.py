# 0725

# 화폐구성

# N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록

# 이때 각 화폐는 몇개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 첫째 줄에 최소한의 화폐 개수를 출력 
# 불가능한 경우 -1 출력

n, m = map(int,input().split())

# 문제 해설 
# 그리디 문제와 거의 동일, 단지 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니라는 점
# 그리디 알고리즘을 사용했던 예시처럼 가장 큰 화폐 단위부터 처리하는 방법으로는 해결할 수 없고  다이나믹 프로그래밍을 적용해야하는 문제
# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾으면 된다.
# 그액 i 를 만들 수 있는 최소한의 화폐 개수를 ai, 화폐의 단위를 k라고 했을 경우
# ai-k를 만드는 방법이 존재하는 경우 ai = min(ai, ai-k + 1)
# 만드는 방법이 없는 경우 a= 10001

array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]]!= 10001 :# i-k 원을 ㄴ만드는 방법이 존재하는 경우?
            d[j] = min(d[j],d[j-array[i]+1])


# if 계산된 결과 출력
if d[m] == 10001 :
    print(-1)
else:
    print(d[m])

