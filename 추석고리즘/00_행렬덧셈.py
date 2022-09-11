# 2738
"""
"""
import sys
sys.stdin = open("행렬덧셈.txt")

N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# pprint(A)
# pprint(B)
answer = [[0] * M for _ in range(N)]
# print(answer)

for r in range(N):
      
      for c in range(M):
            a = A[r][c]
            b = B[r][c]
            
            answer[r][c] = a + b
            
for _ in range(N):
  print(*answer[_])