# 给你一个二维整数数组 matrix， 返回 matrix 的 转置矩阵 。
#
#  矩阵的 转置 是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
#
#
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[1,4,7],[2,5,8],[3,6,9]]
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,2,3],[4,5,6]]
# 输出：[[1,4],[2,5],[3,6]]
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 1000
#  1 <= m * n <= 10⁵
#  -10⁹ <= matrix[i][j] <= 10⁹
#
#
#  Related Topics 数组 矩阵 模拟 👍 324 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        for j in range(n):
            tmp = []
            for i in range(m):
                tmp.append(matrix[i][j])
            res.append(tmp)
        return res

# leetcode submit region end(Prohibit modification and deletion)
