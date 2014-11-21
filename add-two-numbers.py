# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @return a ListNode
	def addTwoNumbers(self, l1, l2):
		current1 = l1
		current2 = l2
		carry = 0
		result = None
		current = None
		while current1 != None and current2 != None:
			mysum = current1.val + current2.val + carry
			carry = mysum / 10
			mysum = mysum % 10
			temp = ListNode(mysum)
			#print carry,mysum
			if current == None:
				current = temp
				result = temp
			else:
				current.next = temp
				current = temp
			current1 = current1.next
			current2 = current2.next


		rest = None
		if current1 == None and current2 == None:
			if carry == 1 :
				temp = ListNode(1)
				current.next = temp
		elif current1 != None:
			rest = current1
		else:
			rest = current2
		currentrest = rest
		while currentrest != None:
			mysum = currentrest.val + carry
			carry = mysum / 10
			mysum = mysum % 10
			temp = ListNode(mysum)
			if current == None:
				current = temp
				result = temp
			else:
				current.next = temp
				current = temp
			currentrest = currentrest.next
		if carry == 1:
			temp = ListNode(1)
			current.next = temp
		return result

	def printll(self,ll):
		i = 0
		while ll != None:
			if i > 10:
				break
			#print ll.val
			i = i + 1
			ll = ll.next



a = ListNode(1)
#b = ListNode(4)
#c = ListNode(3)
#a.next =b 
#b.next = c

d = ListNode(9)
e = ListNode(9)
f = ListNode(9)
d.next = e
e.next = f

s = Solution()
result = s.addTwoNumbers(a,d)
s.printll(result)

