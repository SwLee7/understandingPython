def solution(n, words):
    answer = [0,0]
    count = 0
    add = []
    add.append(words[0])
    for i in range(1, len(words)):
        count += 1
        if words[i] not in add and list(words[i-1])[-1] == list(words[i])[0]:
            add.append(words[i])
        else:
            answer[0] = count % n + 1
            answer[1] = count // n + 1
            break
    return answer