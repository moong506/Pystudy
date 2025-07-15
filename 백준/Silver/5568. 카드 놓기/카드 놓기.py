import sys
from itertools import permutations
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [sys.stdin.readline().strip() for _ in range(n)]
newSet = set()
for nums in permutations(arr, k):
    newString = ''
    for num in nums:
        newString += num
    newSet.add(newString)
print(len(newSet))


