# 문제 설명
# 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT

# 입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

# solution
def solution(a, b):
    answer = 0
    # answer = 0으로 초기화
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    # days를 []에 'FRI'부터 넣고 시작한다. 그 이유는 2016.1.1이 금요일이라는 조건을 주었기 때문이다.
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    # 각 달에 마지막 날을 넣은 리스트를 만든다.
    
    for i in range(a-1):
        # a-1 만큼의 길이를 도는 동안 (0부터 11이 인덱스니까)
        answer += months[i]
        # answer에 months 리스트의 i번 째 요소를 더해간다.
        # 이렇게 하면 달이 계속 더해져 가는 효과를 볼 수 있다.
    
    answer += b-1
    # answer에 입력으로 주어진 b(일)을 더한다.
    # 여기서 b가 아닌 b-1을 하는 이유는 0부터 시작하기 때문이다.
    answer = answer % 7
    # answer를 answer / 7한 나머지로 둔다.
    
    return days[answer]
# days 리스트에서 [answer]째 값을 리턴한다.