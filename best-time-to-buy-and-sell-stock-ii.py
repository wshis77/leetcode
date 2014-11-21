class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		i = 0
		size = len(prices)
		buy = None
		sell = None
		result = 0
		direction = []
		while i < size:
			if i+1 == size:
				direction.append("DOWN")
			else:
				if prices[i] < prices[i+1]:
					direction.append("UP")
				else:
					direction.append("DOWN")
			i = i + 1
		i= 0
		while i < size:
			while i < size and direction[i] == "DOWN":
				i = i + 1
			if i >= size:
				buy = None
			else:
				buy = prices[i]
				#print "buy " + str(buy)
			i = i + 1

			while i < size and direction[i] == "UP":
				i = i + 1
			if i >= size:
				sell = None
			else:
				#print "i " + str(i) 
				sell = prices[i]
				#print "sell " + str(sell)
			i = i + 1
			if buy != None and sell != None:
				result = result + sell - buy
		return result

s = Solution()
print s.maxProfit([1,3,2,4,6,1,-1])

				



			




