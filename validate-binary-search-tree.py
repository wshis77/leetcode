# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		if root == None:
			return True
		if root.left != None:
			if root.val < root.left.val:
				return False
			if not isValidBST(root.left):
				return False
		if root.right != None:
			if root.val > root.right.val:
				return False
			if not isValidBST(root.right):
				return False
		return True
