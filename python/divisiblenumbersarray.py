# 나누어 떨어지는 숫자 배열
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.
# 입출력 예
# arr	        divisor	    return
# [5, 9, 7, 10]	    5	    [5, 10]
# [2, 36, 1, 3]	    1	    [1, 2, 3, 36]
# [3,2,6]	        10	    [-1]
# 입출력 예 설명
# 입출력 예#1
# arr의 원소 중 5로 나누어 떨어지는 원소는 5와 10입니다. 따라서 [5, 10]을 리턴합니다.

# 입출력 예#2
# arr의 모든 원소는 1으로 나누어 떨어집니다. 원소를 오름차순으로 정렬해 [1, 2, 3, 36]을 리턴합니다.

# 입출력 예#3
# 3, 2, 6은 10으로 나누어 떨어지지 않습니다. 나누어 떨어지는 원소가 없으므로 [-1]을 리턴합니다.

# solution
def solution(arr, divisor):
    result = []
    # append할 빈 리스트를 만든다.
    for i in arr:
        # arr을 순회하면서
        if i % divisor == 0:
            # divisor로 i를 나누었을 때 나머지가 0이라면k
            result.append(i)
            # element i를 result에 append한다.
            result.sort()
            # result 리스트를 오름차순 정렬해준다.
    if len(result) == 0:
        # 만약 result의 길이가 0이라면 == arr을 순회하면서 i % divisor == 0의 조건에 맞는 element가 하나도 없으면
        result.append(-1)
        # result 리스트에 -1을 append한다.
    
    return result
    # result를 return 한다.