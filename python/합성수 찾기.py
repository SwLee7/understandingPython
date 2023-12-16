# 문제 설명
# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 100
# 입출력 예
# n	result
# 10	5
# 15	8
# 입출력 예 설명
# 입출력 예 #1

# 10 이하 합성수는 4, 6, 8, 9, 10 로 5개입니다. 따라서 5를 return합니다.
# 입출력 예 #1

# 15 이하 합성수는 4, 6, 8, 9, 10, 12, 14, 15 로 8개입니다. 따라서 8을 return합니다.

# solution
def solution(n):
    answer = 0
    for i in range(n+1):
    # i가 n까지 도는 동안에
        cnt = 0
        # cnt = 0으로 초기화한다.
        for j in range(1, i+1):
        #  j가 1부터 i까지 돌고 있다.
            if i % j == 0:
            # j가 i의 약수라면
                cnt += 1
                # cnt에 1을 추가한다.
        if cnt >= 3:
        # 이 때 cnt가 3을 넘어가면 
            answer += 1
            # answer에 1을 더해나간다.
    return answer