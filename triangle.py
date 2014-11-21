class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		size = len(triangle)
		if size == 0:
			return 0
		elif size == 1:
			return triangle[0][0]

		sum = triangle[0]
		i = 1
		while i < size:
			sum = self.add(sum,triangle[i])
			#print sum
			i = i + 1
		return min(sum)

		

	def add(self, pre,current):
		sum = [] 
		sizeA = len(pre)
		sizeB = len(current)
		i = 0
		while i < sizeB:
			if i == 0:
				sum.append(current[i]+pre[i])
			elif i == sizeB-1:
				sum.append(current[i] + pre[i-1])
			else:
				sum.append(min(current[i] + pre[i],current[i]+ pre[i-1]))
			i = i + 1
		return sum
		
		

s = Solution()
print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
