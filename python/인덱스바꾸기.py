# 문제 설명
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때,
#  my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.

# solution
def solution(my_string, num1, num2):
    arr = list(my_string)
    # my_string을 리스트로 바꾼다.
    arr[num1], arr[num2] = arr[num2], arr[num1]
    # arr(my_string을 리스트화 한 변수)를 swap을 통해 둘을 바꿔준다.
    return ''.join(arr)
# arr을 다시 문자열로 만들어준다.