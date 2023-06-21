# 영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.
# 1 ≤ str의 길이 ≤ 20
# str은 알파벳으로 이루어진 문자열입니다.

# 풀이 방법 1 for문을 이용해 각 요소를 체크하여 대소문자 바꿔주기
str = input()

def solution(str):
    convert = ""
    for i in str:
        if i.isupper():
            convert += i.lower()
        else : convert += i.upper()
    return convert

answer = solution(str)
print (answer)

# 풀이 방법 2 내장 메서드 사용
print (str.swapcase())
