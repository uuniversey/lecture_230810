

# 피보나치1

# def fibo(n):
#     global cnt
#     cnt += 1
#     if n < 2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)
#
#
# cnt = 0
# print(fibo(13), cnt)



# 피보나치2


# def fibo(n):
#     global cnt
#     if n < 2:
#         cnt += 1
#         return memo[n]
#
#     else:
#         if memo[n] == 0:
#             memo[n] = fibo(n-1) + fibo(n-2)
#             cnt += 1
#         return memo[n]
#
#
# cnt = 0
# N = 30
# memo = [0] * (N+1)
# memo[0] = 0
# memo[1] = 1
# print(fibo(N), cnt)



# 피보나치 3


# def fibo(n):
#     dp = [0] * (n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
#
# print(fibo(100))



# 그래프 탐색 기본

# def dfs(n, N, maxtrix):
#     stack = []  # stack 생성
#     visited = [0] * (N+1)   # visited 생성
#     visited[n] = 1  # 시작점 방문 표시
#     print(n)    # do[n]
#     while True:
#         for k in range(1, N+1):   # 현재 정점 n에서 인접하고 미방문 w 찾기
#             if maxtrix[n][k] == 1 and visited[k] == 0:
#                 stack.append(n)  # push(n),  = k
#                 n = k
#                 print(n)    # do(k)
#                 visited[n] = 1  # k 방문 표시
#                 break   # for k, n에 인접인 k 잦은 경우
#         else:
#             if stack:   # stack에 지나온 정점이 남아있으면
#                 n = stack.pop() #pop()해서 다시 다른 k를 찾을 n 준비
#             else:          # 스택이 비어 있으면
#                 break       # while True 탐색 끝
#     return
#
#
# T = 1
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#     matrix = [[0]*(N+1) for _ in range(N+1)]
#
#     for i in range(M):
#         n1, n2 = arr[2*i], arr[2*i + 1]
#         matrix[n1][n2] = 1
#         matrix[n2][n1] = 1
#
#     dfs(1, N, matrix)



# 스위치 켜고 끄기

N = int(input())  # 스위치 개수
arr = list(map(int, input().split()))  # 원래의 스위치
student = int(input())  # 학생 수

for k in range(student):
    stu_info = list(map(int, input().split()))

    if stu_info[0] == 1:  # 남학생 스위치 규칙
        for i in range(1, N + 1):
            if stu_info[1] * i <= N:  # 입력받은 숫자의 배수 부분을 스위칭한다.

                if arr[(stu_info[1] * i) - 1] == 1:  # 0이면 1로 1이면 0으로
                    arr[(stu_info[1] * i) - 1] = 0
                else:
                    arr[(stu_info[1] * i) - 1] = 1

    elif stu_info[0] == 2:  # 여학생 스위치 규칙

        if arr[stu_info[1] - 1] == 0:  # 일단 입력값 부분은 무조건 바꾸니까 0이면 1로 1이면 0으로
            arr[stu_info[1] - 1] = 1
        else:
            arr[stu_info[1] - 1] = 0

        for j in range(1, N):
            if 0 <= (stu_info[1] - 1 - j) and (stu_info[1] - 1 + j) < N:
                if arr[stu_info[1] - 1 - j] == arr[stu_info[1] - 1 + j]:
                    # 입력값 부분의 양쪽이 같다면 걔내도 바꾼다.

                    if arr[stu_info[1] - 1 - j] == 0:  # 0이면 1로 1이면 0으로
                        arr[stu_info[1] - 1 - j] = 1
                    else:
                        arr[stu_info[1] - 1 - j] = 0

                    if arr[stu_info[1] - 1 + j] == 0:  # 0이면 1로 1이면 0으로
                        arr[stu_info[1] - 1 + j] = 1
                    else:
                        arr[stu_info[1] - 1 + j] = 0
                else:
                    break

num = len(arr) // 20  # 20개 이상 스위치를 입력받으면 20개로 끊어서 출력하라고
remain = len(arr) % 20  # 해서 만들었습니다.
if num >= 1:
    for i in range(num):
        print(*arr[20 * i:(20 * i) + 20])
    if remain != 0:  # !!!!!!!!!!!!!!!remain이 0이 될때 문제가 생겼었던 것!!!!!!!!!!!!! 감사합니다 지원님
        print(*arr[-remain:])
else:
    print(*arr)


















