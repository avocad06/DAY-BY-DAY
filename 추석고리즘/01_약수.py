import sys
sys.stdin = open("약수.txt")

int(input())

numbers = list(map(int, input().split()))
numbers = sorted(numbers)
print(numbers[0] * numbers[len(numbers) - 1])