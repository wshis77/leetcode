class Solution:
	# @param root, a tree node
	# @return a list of integers
	def preorderTraversal(self, root):
		result = []
		if root == None:
			return result
		toTraversal = [root]
		while len(toTraversal) > 0:
			head = toTraversal[0]
			result.append(head.val)
			toTraversal.remove(head)
			if head.right != None:
				toTraversal.insert(0,head.right)
			if head.left != None:
				toTraversal.insert(0,head.left)
		return result
			

