import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for j in range(len(arr)-1,-1,-1):
    print (arr[j],end=" ")
