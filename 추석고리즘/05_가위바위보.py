# 2930
"""
"""
import sys
sys.stdin = open("가위보.txt")
from pprint import pprint

rsp_ = ['R', 'S', 'P']

R = int(input())
sang = list(input())
friend = [] # 이중리스트
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
    # 상근이가 가위, 바위, 보
    for rsp in range (len(rsp_)):
        cur = rsp
        # 각 라운드의 각 행별 가위바위보의 점수가
        # 상근이가 어떤 모양응 내면 가장 최대 점수를 받을 수 있을까?
        # 라운드 별로 가위/바위/보 얻을 수 있는 점수
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

r = int(input()) # 라운드
s = input() # 상근이
n = int(input()) # 친구 n명
f = [] # 친구들
for _ in range(n):
    f.append(input())

score = 0 # 점수
max_score = 0 # 최대 점수
srp = {'S' : 0, 'R' : 1, 'P' : 2} # 가위바위보를 숫자로 나타냄

#todo (상근이 - 친구) % 3을 한 결과에 따라 승패가 나뉨
# {'S' : 0, 'R' : 1, 'P' : 2}는 승 == 1, 패 == 2
#? 만약 {'S' : 0, 'P' : 1, 'R' : 2} 했으면 승 == 2, 패 == 1

# 라운드 만큼 반복
for i in range(r):

    # 라운드 마다 상근이가 낼 케이스들 초기화
    srp_case = {'S' : 0, 'R' : 0, 'P' : 0}

    # 친구 n명 반복
    for j in range(n):

        # 이긴 경우 2점 추가
        if (s[i] == 'S' and f[j][i] == 'P') or (s[i] == 'P' and f[j][i] == 'R') or (s[i] == 'R' and f[j][i] == 'S'):
            score += 2
        # 비긴 경우 1점 추가
        elif s[i] == f[j][i]:
            score += 1
        
        #! 진 경우 만들어서 continue 해버리면 밑에 for문 생략됨..
        
        # 가위바위보 반복
        for k in srp:

            # 딕셔너리로 접근해서 이긴 경우 2점 추가
            if (srp[k]-srp[f[j][i]]) % 3 == 1:
                srp_case[k] += 2

            # 비긴 경우 1점 추가
            elif (srp[k]-srp[f[j][i]]) % 3 == 0:
                srp_case[k] += 1

    # 친구 n명 반복 다 끝나고 딕셔너리 밸류 최대값을 저장함
    max_score += max(srp_case.values())

print(score, max_score, sep='\n')