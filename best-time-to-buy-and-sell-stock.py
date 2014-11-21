class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		min = None 
		max = 0
		for p in prices:
			if min == None :
				min = p
			else:
				if p < min: 
					min = p
				current = p - min
				if max < current:
					max = current
		return max



s = Solution()
print s.maxProfit([1,2,3,4,5,6])

