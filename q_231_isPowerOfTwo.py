# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
#  如果存在一个整数 x 使得 n == 2ˣ ，则认为 n 是 2 的幂次方。
#
#
#
#  示例 1：
#
#
# 输入：n = 1
# 输出：true
# 解释：2⁰ = 1
#
#
#  示例 2：
#
#
# 输入：n = 16
# 输出：true
# 解释：2⁴ = 16
#
#
#  示例 3：
#
#
# 输入：n = 3
# 输出：false
#
#
#
#
#  提示：
#
#
#  -2³¹ <= n <= 2³¹ - 1
#
#
#
#
#  进阶：你能够不使用循环/递归解决此问题吗？
#
#  Related Topics 位运算 递归 数学 👍 808 👎 0
import math

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # 最简单的调库做法，先开根号取整之后再平方回来
        # return True if n >0 and 2**(int(math.log(n,2))) == n else False

        # 移位，因为符合要求的数一定2进制只有1个1，例如
        # 8 = 0b1000
        # 8-1 = 7 = 0b111
        # 8&7 == 0
        return True if n>0 and n&(n-1)==0 else False
# leetcode submit region end(Prohibit modification and deletion)
