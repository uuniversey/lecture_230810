

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


def man(num, my_list):
    for i in range(l_arr):
        my_list[num * i]


N = int(input())
arr = list(map(int, input().split()))
l_arr = len(arr)
student = int(input())
stu_info = list(map(int, input().split()))

if stu_info[0] == 1:
    stu_info[1]
elif stu_info[0] == 2:
    stu_info[1]



























