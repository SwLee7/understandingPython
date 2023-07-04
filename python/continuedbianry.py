# 문제 설명
# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

# x의 모든 0을 제거합니다.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
# 예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 x = "0111010" -> "1111" -> "100" 이 됩니다.

# 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# s의 길이는 1 이상 150,000 이하입니다.
# s에는 '1'이 최소 하나 이상 포함되어 있습니다.   

# 입출력 예
#   s	            result
# "110010101001"	[3,8]
# "01110"	        [3,3]
# "1111111"	        [4,1]

# solution
def solution(s):
    answer =[]
    cnt = 0 
    # 이진법으로 변환하는 첫 횟수는 0 이므로 cnt = 0
    zero = 0
    # zero는 0을 빼낸 개수
    while True :
        # 반복문을 도는 동안
        if s == '1':
            # s가 1이 나오면
            break
        # 탈출조건을 달아준다.
        zero += s.count('0')
        # 1이 아니라면 s내에 0의 개수를 세서 zero에 더해준다.
        s = s.replace('0','')
        # 그 후 '0'을 ''(빈칸)으로 바꿔준다. == '0'을 빼준다.
        s = bin(len(s))[2:]
        # s의 길이에 이진변환한 후 앞에 2개 "0b"를 제외한 이진수로 만들어준다.
        cnt += 1
        # 변환 회수를 1 증가 시킨다.
        # break를 이용해 탈출 전까지 반복
        answer = [cnt, zero]
        # 리스트화 시킨후 리턴해준다.
    return answer
