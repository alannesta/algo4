"""
Given a collection of numbers, return all possible permutations.

For example, [1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].


Details:

This solution is recursion with brute force (no prune), no track of current index!
Compare the for loop with combination.py

complexity: O(n*n!)
"""
import copy


def helper(input, curPath, result):
    if len(curPath) == len(input):
        result.append(curPath)
        return

    for i in range(0, len(input)):
        if input[i] not in curPath:   # O(n)
            curPath.append(input[i])
            helper(input, copy.copy(curPath), result)
            curPath.pop()


def permutation(input):
    result = []
    helper(input, [], result)
    return result


if __name__ == "__main__":
    input = [1, 2, 3, 4]

    print(len(permutation(input)))
