# 1546
"""
"""
import sys
sys.stdin = open("평균.txt")

N = int(input())
score = list(map(int, input().split()))
mx = max(score)
answer = 0
for num in score:
    answer += (num/mx) * 100
    
print(answer/N)