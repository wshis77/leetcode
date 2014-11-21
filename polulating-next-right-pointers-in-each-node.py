# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root == None:
			return
		head = root
		while head != None:
			current = head
			while(current != None and current.left != None):
				current.left.next = current.right
				if current.next != None:
					current.right.next = current.next.left
				current = current.next
			head = head.left
		

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

s = Solution()
s.connect(a)
