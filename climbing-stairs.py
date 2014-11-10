class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		if n == 1:
			return 1
		if n == 2: 
			return 2
		else :
			prepre = 1
			pre = 2
			current = 0
			for i in range(0,n-2):
				current = prepre + pre
				prepre = pre
				pre = current
				#print i, current
			return current


s = Solution()
print s.climbStairs(35)


	
					        
