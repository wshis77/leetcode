class Solution:
	# @return a boolean
	def isValid(self, s):
		l = []
		for c in s:
			l.append(c)
			self.push(l)
		if(len(l)==0):
			return True
		else:
			return False
	def push(self,l):
		if len(l) < 2:
			return
		last = l[len(l)-1]
		last2 = l[len(l)-2]
		if(last == ")" and last2 == "("):
			l.pop()
			l.pop()
		if(last == "]" and last2 == "["):
			l.pop()
			l.pop()

		if(last == "}" and last2 == "{"):
			l.pop()
			l.pop()
		

		
s = Solution()
print(s.isValid("{[]][][][][][]{}}{}{}{}{}"))
