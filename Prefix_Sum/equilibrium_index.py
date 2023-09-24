'''
Problem Description:
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

Note:

    Array indexing starts from 0.
    If there is no equilibrium index then return -1.
    If there are more than one equilibrium indexes then return the minimum index.

Problem Constraints:
1 <= N <= 105
-105 <= A[i] <= 105

Example Input:
Input
A = [-7, 1, 5, 2, -4, 3, 0]
Output
3
'''

def Solution(A):
    N = len(A)
    pfSum = [0] * N 
    pfSum[0] = A[0]

    for i in range(0, N):
        if i == 0 and pfSum[i] == pfSum[N-1]:
            return i
        elif pfSum[i] == pfSum[N-1] - pfSum[i-1]:
            return i

    return -1

if __name__ == '__main__':
    A = [-7, 1, 5, 2, -4, 3, 0]
    Solution(A)

