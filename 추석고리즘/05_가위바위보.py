# 2930
"""
"""
import sys
sys.stdin = open("가위보.txt")
from pprint import pprint

rsp_ = ['R', 'S', 'P']

R = int(input())
sang = list(input())
friend = []
# 현재 상근
origin = 0
N = int(input())
    
for r in range(N):
    friend.append(list(input()))
    # print(friend)

for rnd in range(R):
    for idx in range(N):
        cur = sang[rnd]
        frs = friend[idx][rnd]
        
        if cur == frs:
            origin += 1
        
        elif cur == 'R':
            if frs == 'S':
                origin += 2
                
        elif cur == 'S':
            if frs == 'P':
                origin += 2
                
        elif cur == 'P':
            if frs == 'R':
                origin += 2

print(origin)

    # print(cur)

score = 0
mx_score = 0
for rnd in range(R):
    rsp_score = [0, 0, 0]
    for rsp in range (len(rsp_)):
        cur = rsp
        # 각 라운드의 각 행별 가위바위보의 점수가
        # 상근이가 어떤 모양응 내면 가장 최대 점수를 받을 수 있을까?
        for idx in range(N):
            frs = friend[idx][rnd]
        
            if rsp_[cur] == frs:
                rsp_score[cur] += 1
        
            elif rsp_[cur] == 'R':
                if frs == 'S':
                    rsp_score[cur] += 2
                    
            elif rsp_[cur] == 'S':
                if frs == 'P':
                    rsp_score[cur] += 2
                    
            elif rsp_[cur] == 'P':
                if frs == 'R':
                    rsp_score[cur] += 2
                    
        # print(rsp_[rsp], rsp_score)
    rnd_score = max(rsp_score)
    mx_score += rnd_score
        # score = max(score, rsp_score)
    # mx_score += score

print(mx_score)


                

# for c in range(int(input())):
#     friend.append(list(input()))
#     pprint(friend)
#     for r in range(R):
#         frs = friend[c][r]
#         # print(frs, r)
#         for rsp in sang:
#             if rsp == frs:
#                 origin += 1
#                 break
#             if rsp == 'S':
#                 if frs == 'P':
#                     origin += 2
                    
#             elif rsp == 'R':
#                 if frs == ''