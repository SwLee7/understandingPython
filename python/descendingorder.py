# 정수 내림차순으로 배치하기

# 함수 solution은 정수 n을 매개변수로 입력받습니다. 
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 나의 풀이
def solution(n):
    li = list(str(n))
    # 정수를 문자열로 바꾼 뒤 배열화
    li.sort()
    li.reverse()
    # list를 오름차순 정렬 및 뒤집기 => ["5","4","3","2","1"]
    result = "".join(li)
    # list를 문자열로 바꿔주고
    return int(result)
    # 문자열을 정수의 형태로 바꿔주기


# 구글링한 다른 사람들의 풀이
def solution2(n) :
    li2 = list(str(n))
    li2.sort(reverse = True)
    # reverse = True로 만들어주는 sort()를 사용하면 역순 정렬을 해준다.
    result2 = ''.join(li2)
    return int(result2)