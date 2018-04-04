"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

Source: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#DO NOT CHANGE THIS CLASS
class Solution(object):
    def sortedArrayToBST(self, nums):
        
        # Check if the array is empty
        if not nums:
            return None
        
        # Recursive: start with midpoint and apply left & right
        else:
            middle = len(nums)//2
            
            root = TreeNode(nums[middle])
            root.right = self.sortedArrayToBST(nums[middle+1:])
            root.left = self.sortedArrayToBST(nums[:middle])
            
            return root

