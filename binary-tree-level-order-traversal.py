# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrder(self, root):
		if root == None:
			return []
		parent = [root]
		children = []
		result = []
		while len(parent) > 0:
			temmp = []
			children = []
			for p in parent:
				temp.append(p.val)
				if(p.left != None):
					children.append(p.left)
				if(p.right != None):
					children.append(p.right)
			result.append(temp)
			parent = children
		return result







