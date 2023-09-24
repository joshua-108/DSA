'''
Problem Description:
Given an array, arr[] of size N, the task is to find the count of array indices such that
removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Problem Constraints:
1 <= n <= 105
-105 <= A[i] <= 105

Input Format:
First argument contains an array A of integers of size N.

Output format:
Return the count of array indices such that removing an element
from these indices makes the sum of even-indexed and odd-indexed array elements equal.

Example
input:
A=[2, 1, 6, 4]

output:
1
Removing arr[1] from the array modifies arr[] to { 2, 6, 4 } such that, arr[0] + arr[2] = arr[1].
Therefore, the required output is 1.
'''

N = len(A)
pfEven = [0] * N
pfEven[0] = A[0]
pfOdd = [0] * N

#prefix sum of even index
for i in range(1, N):
    if i%2 == 0:
        pfEven[i] = pfEven[i-1] + A[i]
    else:
        pfEven[i] = pfEven[i-1]

for i in range(1, N):
    if i%2 != 0:
        pfOdd[i] = pfOdd[i-1] + A[i]
    else:
        pfOdd[i] = pfOdd[i-1]

count = 0
for i in range(0, N):
    Se = pfOdd[N-1] - pfOdd[i]
    So = pfEven[N-1] - pfEven[i]

    if i!=0:
        Se = Se + pfEven[i-1]
        So = So = pfOdd[i-1]

    if Se == So:
        count += 1

print(count) 

#TC = O(N)
#SC = O(N)
