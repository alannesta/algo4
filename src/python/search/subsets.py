"""

Given a set of distinct integers, S, return all possible subsets.
Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.

For example, If S = [1,2,3], a solution is:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


Solution:

1. 状态转移图: select or not select --> unbalanced binary tree
2. DFS for binary tree traversal (draw the traversal graph on paper)


Details:

copy.copy(curPath)

"""
import copy


def helper(input, curPath, curIndex):
    if curIndex == len(input) - 1:
        result.append(curPath)
        return

    # case 1: not select element curIndex
    helper(input, curPath, curIndex + 1)

    # case 2: select element curIndex
    curPath.append(input[curIndex]) # add the cur element
    helper(input, copy.copy(curPath), curIndex + 1)    # copy of curPath
    curPath.pop()  # remove the cur element


def combination(input):
    helper(input, [], 0)


if __name__ == "__main__":
    input = [1, 2, 3, 4]
    result = []

    combination(input)
    print(result)

