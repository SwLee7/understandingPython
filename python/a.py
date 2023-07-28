row = int(input('별을 출력할 줄의 수:'))

for i in range (row+1):
    for j in range(i+1):
        print('*', end='')
    print('')