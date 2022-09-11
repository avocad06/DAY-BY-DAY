# 1855
"""
"""
import sys
sys.stdin = open("암호.txt")

column = int(input())
password = input()
row = len(password) // column
# print(row)

table = []
for word in range(0, len(password), column):
    small_table = []
    table.append(small_table)
    
    for idx in range(column):
        small_table.append(password[word + idx])
        

# print(table)
answer = ''
for c in range(column):
    
    for r in range(row):
        
        if (r + 1) % 2 != 0:
            answer += table[r][c]
        
        elif (r + 1) % 2 == 0:
            answer += table[r][column-1 -c]
            
print(answer)
        

