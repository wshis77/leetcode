# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		i1 = l1
		i2 = l2
		head = ListNode()
		end = head 
		while i1 != None and i2 != None:
			if(i1.val < i2.val):
				temp = ListNode()
				temp.val = i1.val
				end.next = temp
				end = temp
				i1 = i1.next
			else:
				temp = ListNode()
				temp.val = i2.val
				end.next = temp
				end = temp
				i2 = i2.next
		if i1 == None and i2 == None:
			return head.next
		elif i1 != None:
			while i1 != None:
				temp = ListNode()
				temp.val = i1.val
				end.next = temp
				end = temp
				i1 = i1.next
			return head.next
		else:
			while i2 != None:
				temp = ListNode()
				temp.val = i2.val
				end.next = temp
				end = temp
				i2 = i2.next
			return head.next

