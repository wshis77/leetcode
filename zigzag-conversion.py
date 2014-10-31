class Solution:
	# @return a string
	def convert(self, s, nRows):
		if nRows == 1:
			return s
		size = len(s)
		num = nRows-1
		UP = True
		data = {}
		for j in range(0,nRows):
			data[j] = []
		index = 1 
		for i in range(0,size):
			if UP:
				index = index - 1
				data[index].append(s[i])
			else:
				index = index + 1
				data[index].append(s[i])
			#print i, index
			if i % num == 0:
				UP = not UP
		result = []
		for j in range(0,nRows):
			result.append("".join(data[j]))
		return "".join(result)

s = Solution()
print( s.convert("PAYPALISHIRING",3))

