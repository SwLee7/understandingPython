# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ my_string 안의 자연수 ≤ 1000
# 연속된 수는 하나의 숫자로 간주합니다.
# 000123과 같이 0이 선행하는 경우는 없습니다.
# 문자열에 자연수가 없는 경우 0을 return 해주세요.
# 입출력 예
# my_string	result
# "aAb1B2cC34oOp"	37
# "1a2b3c4d123Z"	133
# 입출력 예 설명
# 입출력 예 #1

# "aAb1B2cC34oOp"안의 자연수는 1, 2, 34 입니다. 따라서 1 + 2 + 34 = 37 을 return합니다.
# 입출력 예 #2

# "1a2b3c4d123Z"안의 자연수는 1, 2, 3, 4, 123 입니다. 따라서 1 + 2 + 3 + 4 + 123 = 133 을 return합니다.
# solution
import re
# 정규 표현식을 import
def solution(my_string):
    my_string = re.sub('[a-zA-Z]',' ',my_string)
    # my_string에서 숫자를 제외한 모든 문자열을 공백으로 만든다.
    num_list = list(map(int, my_string.split()))
    # map을 이용해 my_string에 있는 모든 요소를 int형으로 바꿔준다.
    return sum(num_list)
    # num_list의 합을 리턴한다.