# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# solution

def solution(answers):
    answer = []
    first_man_score, second_man_score, third_man_score = 0,0,0

    first_man = [1,2,3,4,5]
    second_man = [2, 1, 2, 3, 2, 4, 2, 5]
    third_man = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first_man[i % len(first_man)]:
            first_man_score += 1
        if answers[i] == second_man[i % len(second_man)]:
            second_man_score += 1
        if answers[i] == third_man[i % len (third_man)]:
            third_man_score += 1

    highest_score = max(first_man_score, second_man_score, third_man_score)

    if highest_score == first_man_score:
        answer.append(1)

    if highest_score == second_man_score:
        answer.append(2)

    if highest_score == third_man_score:
        answer.append(3)

    return answer