#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
	
		if head == None:
			return None
		saveHead = head
		lengthFromHead = self.length(head) - n
		if(lengthFromHead == 0):
			result = head.next
			del head
			return result
		print lengthFromHead
		current = head
		for i in range(0,lengthFromHead-1):
			current = current.next
		currentNext= current.next
		if currentNext.next == None:
			current.next = None
			del currentNext
		else:
			current.next = currentNext.next
			del currentNext
		return saveHead
		
				        
	def length(self,head):
		temp = head
		i = 0
		while(temp!= None):
			i = i+ 1
			temp = temp.next
		return i

a = ListNode(1)
b = ListNode(2)
a.next = b

s = Solution()
s.removeNthFromEnd(a,1)
