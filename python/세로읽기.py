# 문제 설명
# 문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# my_string은 영소문자로 이루어져 있습니다.
# 1 ≤ m ≤ my_string의 길이 ≤ 1,000
# m은 my_string 길이의 약수로만 주어집니다.
# 1 ≤ c ≤ m
# 입출력 예
# my_string	m	c	result
# "ihrhbakrfpndopljhygc"	4	2	"happy"
# "programmers"	1	1	"programmers"
# 입출력 예 설명
# 입출력 예 #1

# 예제 1번의 my_string을 한 줄에 4 글자씩 쓰면 다음의 표와 같습니다.

# 1열	2열	3열	4열
# i	h	r	h
# b	a	k	r
# f	p	n	d
# o	p	l	j
# h	y	g	c
# 2열에 적힌 글자를 세로로 읽으면 happy이므로 "happy"를 return 합니다.

# 입출력 예 #2

# 예제 2번의 my_string은 m이 1이므로 세로로 "programmers"를 적는 것과 같고 
# 따라서 1열에 적힌 글자를 세로로 읽으면 programmers입니다. 따라서 "programmers"를 return 합니다.

# solution
def solution(my_string, m, c):
    return my_string[c-1:len(my_string):m]
# my_string에서 c-1부터 시작하여 my_string을 순회하면서 m만큼의 간격을 두고 리턴해주세요.
# len(my_string)는 없어도 무방함. ==> 이유는 어차피 len(my_string)까지 m 간격 만큼만 두고 끝날 것이기 때문이지.