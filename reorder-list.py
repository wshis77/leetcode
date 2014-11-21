#Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		reverseList = []
		current = head
		while current != None:
			reverseList.insert(0,current)
			current = current.next
		
		current = head
		i = 0
		size = len(reverseList)
		for i in range(0,size):
			print "iii " + str(i)
			if current == reverseList[i]:
				current.next = None
				break
			if current.next == reverseList[i]:
				reverseList[i].next = None
				break
			reverseList[i].next = current.next
			current.next = reverseList[i]
			current = reverseList[i].next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
s = Solution()
s.reorderList(a)
while a != None:
	print a.val
	a = a.next



					        
