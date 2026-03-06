import sys
sys.stdin = open("input_bi2.txt", "r")

T = int(input())
for t_c in range(1, T+1):
    N = float(input())

    if N == 0:
        print(f'#{t_c} {0}')
        break

    minus_bi = [0]*13
    flo = 0.5

    for i in range(1, 13):
        minus_bi[i] = flo
        flo /= 2

    result = ''


    for i in range(1 << 12):
        rev_binary = '0'
        while i>0:
            if i%2 == 0:
                rev_binary += '0'
            else:
                rev_binary += '1'
            i = i // 2

        # print('진법', rev_binary)

        flo_sum = 0

        for j in range(1, len(rev_binary)):
            if rev_binary[j] == '1':
                flo_sum += minus_bi[j]

        # reversed(rev_binary)
        # print('진법', rev_binary)
        # print(flo_sum)

        if flo_sum == N:
            result += rev_binary[1::]
            break

    if result == '':
        result = 'overflow'

    print(f'#{t_c} {result}')










