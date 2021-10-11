"""
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


# dp
def solution(word1, word2):
    l1 = len(word1) + 1
    l2 = len(word2) + 1

    dp = []

    for i in range(l2):
        tmp = []
        for j in range(l1):
            if i == 0:
                tmp.append(j)
            elif j == 0:
                tmp.append(i)
            else:
                tmp.append(max(i, j))

        dp.append(tmp)

    # print(dp)

    for i in range(l1):
        for j in range(l2):
            if i == 0 or j == 0:
                continue

            if word1[i - 1] == word2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(dp[j - 1][i], dp[j][i - 1], dp[j - 1][i - 1]) + 1


    return dp[l2 - 1][l1 - 1]


solution('horse', 'ros')
