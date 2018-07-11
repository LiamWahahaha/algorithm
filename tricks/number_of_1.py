class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn = bin(n)
        return bn.count('1')

print(Solution().hammingWeight(11))
