# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def zigzagLevelOrder(self, root):
		
		left = True
		result = []
		toTraversal = [root]
		while len(toTraversal) > 0:
			size = len(toTraversal)
			temp = []
			if left:
				for i range(0,size):
					temp.append(toTraversal[i].val)
			else:
				for i range(0,size):
					temp.append(toTraversal[size-i].val)
			result.append(temp)
			children = []
			for node in toTraversal:
				if node.left != None:
					children.append(node.left)
				if node.right != None:
					children.append(node.right)
			left = not left
		return result	




