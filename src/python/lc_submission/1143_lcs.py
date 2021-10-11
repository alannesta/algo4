"""
https://leetcode.com/problems/longest-common-subsequence/
Given two strings text1 and text2, return the length of their longest common subsequence.

If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)

deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3

Explanation: The longest common subsequence is "ace" and its length is 3.
"""


# dp
def lcs(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = []
    for i in range(len2 + 1):
        temp = []
        for j in range(len1 + 1):
            temp.append([0])

        dp.append(temp)

    # print(dp)
    for i in range(len2 + 1):
        for j in range(len1 + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if s1[j - 1] == s2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len2][len1]


# recursion
def solution2():
    str1 = 'abcde'
    str2 = 'ace'

    memo = {}

    def walk(i, j):

        if (i, j) in memo:
            return memo[(i, j)]

        # base case
        if i == -1 or j == -1:
            return 0

        if str1[i] == str2[j]:
            memo[(i, j)] = walk(i - 1, j - 1) + 1
            return memo[(i, j)]
        else:
            memo[(i, j)] = max(walk(i, j - 1), walk(i - 1, j))
            return memo[(i, j)]

    return walk(len(str1) - 1, len(str2) - 1)


# print(lcs('abcde', 'ace'))
print(solution2())
