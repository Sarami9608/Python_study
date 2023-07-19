# 230720

# 떡볶이 떡 만들기

# 오늘은 떡볶이 떡을 만드는 날이다. 덕볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다.
# 절단기 높이를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 h보다 긴 떡은 h위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 19,15,14,17 cm의 높이를 가진 떡을 15cm 높이를 가진 절단기로 절단하면 15,15,14,15로 맞추질 것이다. 

# 입력조건
# 첫째 줄에 떡의 개수 n과 요청한 떡의 길이 m이 주어진다.
# 둘째 줄에 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 m 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 가틍ㄴ 양의 정소 또는 0이다.

# 출력 조건
# ㅈ거어도 m만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값ㅇ르 출력한다.


# 문제 해설
# 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형의 문제이다. 
# 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다. ***원하는 조건을 만족하는 가장 알맞은 값ㅇ르 찾는 문제에 주로 파라메트릭 서치를 사용***한다.
# 예를 들어 범위 내에서 조건ㅇ르 만족하느 ㄴ가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.
# 코딩 테스트나 프로그래밍 대회에서는 보통 파라메트릭 서치 유형은 이진 탐색을 이용하여 해결한다.

# 이 문제를 풀기 위한 아이디어는 의외로 간단한다. 적절한 높이를 찾을 때까지 절단기의 높이 h를 반복해서 조정하는 것이다. 그래서 '현재 이 높이로 자르면 조건을 만족할 수 있는가?'를 확인한 뒤에 조건의 만족 여부에 따라서
# 탐색 범위를 좁혀서 해결할 수 있다. 범위를 좁힐 때는 이진 탐색의 원리를 이용하여 절반씩 탐색 범위를 좁혀 나간다. 
# 절단기의 높이는 1부터 10억까지의 정수 중 하나인데 , 이처럼 큰 수를 보면 당연하다는 듯이 가장 먼저 이진 탐색을 떠올려야 한다. 이 문제에서 절단기의 높이 범위가 한정적이었다면 순차 탐색으로도 해결할 수 있지만, 현재 문제에서
# 절단기의 높이는 최대 10억까지이의 정수이므로 순차 탐색은 신간 초과를 할 경우가 존재하게 된다.

# 반면에 높이 h를 이진 탐색으로 찾는다면, 대략 31번 만에 경우의 수를 모두 고려할 수 있다. 이때 떡의 개수 n이 최대 100만 개이므로 이진 탐색으로 절단기의 높이 h를 바꾸면서, 바꿀 때마다 모든 떡을 체크하는 경우 대략 최대 3000만 번 정도의 연산으로 문제를 풀 수 있다.

# 문제의 시간 제한은 2초이므로 최악의 경우 3000만 번 정도의 연상이 필요하다면 아슬아슬하게 시간에 걸리지 않고 정답이 될 것이다.

# 예시 코드

# 떡의 개수n 와 요청한 떡의 길이 m 입력
import sys
n,m = map(int,sys.stdin.readline().split())
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int,sys.stdin.readline().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복을 통한)
result = 0 
while start <= end:
    total = 0
    mid = (start + end) //2
    for x in array:
        if x > array[mid]:
            total += (x - array[mid])
    
    if total == m:
        result = mid
    elif total < mid:
        end = mid -1
    else :
        start = mid +1

print(result)