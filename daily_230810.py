


# 1219. 길찾기

# import sys
# sys.stdin = open('input_1219.txt', 'r')
#
# for tc in range(1, 11):
#     O, road = map(int, input().split())
#     arr = list(map(int, input().split()))
#     matrix = [[0] * 100 for _ in range(100)]        # 인접 행렬 만들기
#     outpoint = 99                                   # 탈출 포인트
#
#     for i in range(road):
#         road1, road2 = arr[2*i], arr[2*i + 1]
#         matrix[road1][road2] = 1                    # 일반통행이니까
#
#     stack = []
#     visit_check = [False] * 100     # 방문 체크
#     me = 0          # 시작점
#     result = 0      # 길 있는지 없는지 초기값
#     visit_check[me] = True
#     num = 0         # 무한 루프 방지 초기값
#
#     while True:
#         num += 1                # 무한 루프 방지
#         if num == 10000:
#             break
#
#         for station in range(100):
#             if matrix[me][station] == 1 and visit_check[station] == False:
#                 stack.append(me)
#                 me = station
#                 visit_check[me] = True
#                 break
#
#         else:
#             if me == outpoint:
#                 result = 1
#                 break
#             else:
#                 if len(stack) != 0:
#                     me = stack.pop()
#                     continue
#
#     print(f'#{tc} {result}')



# 18311. stack 1. 그래프 탐색

# import sys
# sys.stdin = open('input_18311.txt', 'r')
#
# T = 1
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     arr = list(map(int, input().split()))
#     matrix = [[0] * (V+1) for _ in range(V+1)]
#
#     for i in range(E):
#         v1, v2 = arr[2*i], arr[2*i + 1]
#         matrix[v1][v2] = 1
#         matrix[v2][v1] = 1
#
#     stack = []
#     result = []     # 방문한 점을 저장하기 위한 list 나중에 join으로 붙여서 출력할 예정
#     visit_check = [False] * (V+1)   # 정점 0은 사용하지 않으므로 편의상 +1 을 한다.
#     start_point = 1
#
#     result.append(start_point)  # 방문 처리
#     visit_check[start_point] = True
#
#     while True:
#         for j in range(1, V+1):
#             if matrix[start_point][j] == 1 and visit_check[j] == False: # 방문 가능 지점 and 방문 했는지 체크
#                 stack.append(start_point)       # 이전에 방문한 지점을 push
#                 start_point = j
#                 visit_check[start_point] = True     # 방문 여부 체크
#                 result.append(start_point)
#                 break
#
#         else:
#             if len(stack) != 0:
#                 start_point = stack.pop()
#             else:
#                 break
#
#     my_result = "-".join(map(str, result))
#     print(f'#{tc} {my_result}')



# 18227. 그래프 경로

# import sys
# sys.stdin = open('input_18227.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     node, road = map(int, input().split())
#     arr = []
#
#     for i in range(road):                       # 입력이 저 모양이라 입력을 행렬로 받음
#         temp = list(map(int, input().split()))
#         arr.append(temp)
#
#     S, G = list(map(int, input().split()))      # 처음과 끝을 받음
#
#     matrix = [[0] * (node + 1) for _ in range(node + 1)]    # 인접 행렬 생성
#
#     for idx in range(road):
#         road1, road2 = arr[idx][0], arr[idx][1]
#         matrix[road1][road2] = 1
#
#     result = 0
#     stack = []
#     visit_check = [False] * (node + 1)
#     visit_check[S] = True
#
#     while True:
#         for k in range(1, node+1):
#             if visit_check[k] == False and matrix[S][k] == 1:
#                 stack.append(S)
#                 S = k
#                 visit_check[S] = True
#                 break
#
#         else:
#             if G == S:                  # 끝점에 도착했을때
#                 result += 1
#                 break
#             else:
#                 if len(stack) != 0:
#                     S = stack.pop()
#                 else:
#                     break
#
#     print(f'#{tc} {result}')



# 18226. 종이붙이기

# import sys
# sys.stdin = open('input_18226.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     area = 20 * N
#     small_area = 200
#     large_area = 400
#
#     num = area // large_area
#
#     for i in num:
#         area = 20 * N
#         area = area - (large_area * i)
#         small_num = area // small_area          # 작은 블럭 넣어야 하는 갯수
#
#
#
#
#
#     print(f'#{tc} {N}')


# 5432. 쇠막대기 자르기

# import sys
# sys.stdin = open('input_5432.txt', 'r')
#
# T = int(input())
# for tc in range(1, T+1):
#     laser = list(input())
#     stack = []
#     stick = 1
#     stack.append(laser[0])
#
#     for i in range(1, len(laser)):
#
#         if laser[i] == '(':
#             stack.append(laser[i])
#             stick += 1
#
#         elif laser[i] == ')':
#             stack.pop()
#
#             if laser[i-1] == '(' and laser[i] == ')':
#                 stick += len(stack)
#                 stick -= 1
#
#     print(f'#{tc} {stick}')