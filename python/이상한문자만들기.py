# 문제 설명
# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# 제한 사항
# 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
# 입출력 예
# s	return
# "try hello world"	"TrY HeLlO WoRlD"
# 입출력 예 설명
# "try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

# solution
def solution(s):
    answer = ''
    # 리턴할 answer를 빈 문자열로 할당
    s_list = s.split(' ')
    # 빈 문자열을 기준으로 잘라내는 리스트를 만든다.
    for i in s_list:
        # i가 리스트를 순회하면서
        for j in range(len(i)):
            # i의 길이만큼 j가 순회하는데
            if j % 2 == 0:
                # 만약 j가 짝수라면
                answer += i[j].upper()
                # answer에 i[j]의 값을 대문자로 바꿔 더해간다.
            else :
                # 만약 j가 홀수라면
                answer += i[j].lower()
                # answer에 i[j]의 값을 소문자로 바꿔 더해간다.
        answer += ' '
        # answer에 띄어쓰기를한다.
    return answer[0:-1]
    # 이렇게 생긴 answer의 0번 째 인덱스부터 마지막 인덱스의 전까지의 값만 리턴한다.
    # 왜냐하면 answer 전체를 리턴하면 마지막 띄어쓰기까지 리턴하기 때문에 오답이 나온다. ** 주의! 
print (solution('hello world'))