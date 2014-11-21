class Solution:
	def combine(self, n, k):
		S = []
		for i in range(1,n+1):
			S.append(i)
		subsetsCount = pow(2,n) 
		result = []
		for i in range(0,subsetsCount):
			temp = []
			for j in range(0,n):
				if ( i >> j) % 2 == 1:
					temp.append(S[j])
			if len(temp) == k:
				result.append(temp)
		return result

s = Solution()
print s.combine(9,8)
		
					        
