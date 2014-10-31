# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if(head == None or head.next == None):
			return head
		pre = head
		current = None
		temp = head.next
		while temp != None:
			if temp.val == pre.val:
				pre.next = temp.next
				temp = temp.next
			else:
				pre = temp
				temp = temp.next
		return head

