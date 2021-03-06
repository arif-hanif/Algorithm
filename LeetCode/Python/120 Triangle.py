# -*- coding: utf-8 -*-

'''
Triangle
========

Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
- Bonus point if you are able to do this using only O(n) extra space, where n
  is the total number of rows in the triangle.
'''


import collections


class Solution(object):
    '''算法思路：

    动态规划
    '''
    def minimumTotal(self, triangle):
        n = len(triangle)

        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i + 1):
                dp[i][j] = min(
                    dp[i - 1][j],
                    dp[i - 1][j - 1]
                ) + triangle[i][j]

        return min(dp[-1])


class Solution(object):
    '''算法思路：

    简化空间，用队列，每次 pop 出来的对应当前 row 的一个元素
    '''
    def minimumTotal(self, triangle):
        queue, MAX = collections.deque(), float('inf')

        for row in triangle:
            pre = MAX

            for i in xrange(len(queue)):
                queue.append(min(pre, queue[0]) + row[i])
                pre = queue.popleft()

            queue.append([pre, 0][pre == MAX] + row[-1])

        return min(queue)


s = Solution()
print s.minimumTotal([
    [1],
    [2, 3],
    [6, 5, 7]
])
