'''
Problem Description:
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

Problem Constraints:
1 <= N, M <= 105
1 <= A[i] <= 109
0 <= L <= R < N

Input Format:
The first argument is the integer array A.
The second argument is the 2D integer array B.
# @param A : list of integers
# @param B : list of list of integers
# @return an list of long

Example:
input
A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]

output
[10, 5]
'''

#First create a prefix sum array
for i in range(1, len(A)):
    A[i] = A[i-1] + A[i]

result = []
for j in range(0, len(B)):
    s = B[j][0]
    e = B[j][1]
    if s == 0 and e == 0:
        result.append(A[0])
    elif s == 0:
        result.append([A[s]])
    else:
        ans = A[s] - A[e-1]
        result.append(ans)
print(result)

#TC = N+Q
#SC = O(1)