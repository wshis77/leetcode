# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def insertionSortList(self, head):
		current = head
		result = None
		pre = None
		min = None
		while current.next != None:
			if min == None:
				min = current
				pre = None
			else:
				if min.val > current.val:
					min = current
			pre = current
			current = current.next



