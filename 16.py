s=input("ENTER THE NUMBERS : ")
arr=list(map(int,s.split()))

mean = sum(arr) / len(arr)

arr.sort()
if len(arr) % 2 == 0:
    median = (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
else:
    median = arr[len(arr)//2]

from collections import Counter
counter = Counter(arr)
mode = counter.most_common(1)[0][0]

print("Mean: ", mean)
print("Median: ", median)
print("Mode: ", mode)