# 1259
"""
"""
import sys
sys.stdin = open("팰린드롬.txt")



while True:
    words = input()
    words_ = words[::-1]
    
    if words != "0":
        if words_ != words:
            print("no")
    
        elif words_ == words:
            print("yes")
        
    elif words == "0":
        break
