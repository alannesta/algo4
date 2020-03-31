"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example, If n = 4 and k = 2, a solution is:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Solution:

compare with subsets:
状态转移图不再为binary tree. 这种情况下需要for loop

"""
import copy

def helper(input, curPath, curIndex, count, result):
    if len(curPath) == count:
        return result.append(curPath)

    # not needed
    # if curIndex == len(input):
    #     return

    for i in range(curIndex, len(input)):
        curPath.append(input[i])
        helper(input, copy.copy(curPath), i + 1, count, result)
        curPath.pop()


def combination(input, count):
    result = []
    helper(input, [], 0, count, result)
    return result


if __name__ == "__main__":
    input = [1, 2, 3, 4]
    count = 2
    result = combination(input, count)

    print(result)
