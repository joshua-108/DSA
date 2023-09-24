'''
Problem Description:
You have given a string A having Uppercase English letters.
You have to find how many times subsequence "AG" is there in the given string.

Problem Constraints:
1 <= length(A) <= 105

Example Input
Input 1:
 A = "ABCGAG"
Input 2:
 A = "GAB"

Example Output
Output 1:
 3
Output 2:
 0
'''

count_a = 0
ans = 0
for item in A:
    if item == 'A':
        count_a += 1
    if item == 'G':
        ans += count_a

print(ans)

#TC = O(N)
#SC = O(1)