# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 
# 예를 들어
# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# 입출력 예
#   s      answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

# 접근 방법

# ()가 되어야 올바른 괄호.
# 스택에 '('만 넣어두고 ')'가 들어 올때에만 삭제 시킨다.
# 스택이 비어있는데 ')'가 들어오면 올바른 짝이 될 수 없기 때문에 False를 리턴한다.
# for 문을 다 돌았는데 stack안에 '('가 남아 있다면 올바른 짝이 아니기 때문에 False를 리턴한다.

# solution

def solution(s):
    stack = []
    for bracket in s:
        # s를 순회하면서
        if bracket == '(':
            # bracket이 '('이면
            stack.append(bracket)
            # 스택에 '('를 넣어준다.
        elif bracket == ')':
            # 그런데 만약 s가 ')'일 때
            if stack :
                # stack에 '('가 남아 있다면
                stack.pop()
                # stack에서 '('를 지워준다.
            elif stack == []:
                # stack에 '('가 없다면
                return False
            # False를 리턴한다.
        if stack != []:
            # s를 전부 다 순회를 했는데도 stack안에 '('가 남아 있으면
            return False
            # False를 리턴한다.

    return True