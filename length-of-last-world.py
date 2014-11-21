class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLastWord(self, s):
		size = len(s)
		i = size-1
		result = 0
		if size == 0:
			return 0
		while i >= 0:
			current = s[i]
			if current.isalpha() == False:
				i = i - 1
			else:
				break
		if i < 0:
			return 0
		while i >= 0:
			#print current
			current = s[i]
			if current.isalpha():
				result = result + 1
				i = i -1
			else:
				break
		return result

s = Solution()
print s.lengthOfLastWord("a")
