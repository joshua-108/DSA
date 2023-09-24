'''
Problem Description:
 Given an array A, find the size of the smallest subarray such that it contains at 
 least one occurrence of the maximum value of the array
 and at least one occurrence of the minimum value of the array. 

Problem Constraints:
1 <= |A| <= 2000

Example Input
Input:
A = [1, 3, 2]
Output:
2

'''

#first find the min and max from the given list.
_min = min(A)
_mx = max(A)
ans = float('inf')

last_min_index = -1
last_max_index = -1

for i in range(0, len(A)):
    if A[i] == _min:
        if last_min_index != -1:
            length = i-last_min_index+1
            ans = min(ans, length)
        last_min_index = i
    if A[i] == _max:
        if last_max_index != -1:
            length = i-last_max_index+1
            ans = min(ans, length)
        last_max_index = i

print(ans)

#TC = O(N)
#SC = O(1)

