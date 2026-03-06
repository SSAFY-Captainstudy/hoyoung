import sys
sys.stdin = open("simple_code.txt", "r")

code_dic = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
            '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for t_c in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]

    code = ''

    for i in range(N):
        if '1' in arr[i]:
            code = arr[i]
            break

    end = code.rfind('1')

    password = code[end-55:end+1]

    numbers = []

    for i in range(0, 56, 7):
        numbers.append(code_dic[password[i:i+7]])

    odd = numbers[0] + numbers[2] + numbers[4] + numbers[6]
    even = numbers[1] + numbers[3] + numbers[5] + numbers[7]

    if ((odd * 3) + even) % 10 == 0:
        result = odd + even
    else:
        result = 0

    print(f'#{t_c} {result}')






