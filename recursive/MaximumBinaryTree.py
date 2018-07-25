import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums, ret = None):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        idx = nums.index(max(nums))
        left = nums[:idx]
        right = nums[idx + 1:]
        ret = TreeNode(nums[idx])

        if left:
            ret.left = self.constructMaximumBinaryTree(left, ret.left)
        if right:
            ret.right = self.constructMaximumBinaryTree(right, ret.right)

        return ret

def testcase():
    start_time = 0
    elapsed_time = []

    for length in range(1, 1000, 10):
        nums = [val for val in range(length)]
        start_time = time.time()
        Solution().constructMaximumBinaryTree(nums)
        elapsed_time.append(time.time() - start_time)

    plt.plot(elapsed_time)
    plt.ylabel('elapsed_time')
    plt.xlabel('data size')
    plt.show()

if __name__ == '__main__':
    testcase()
