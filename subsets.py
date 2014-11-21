class Solution:
	# @param S, a list of integer
	# @return a list of lists of integer
	def subsets(self, S):
		S.sort()
		size = len(S)
		subsetsCount = pow(2,size) 
		result = []
		for i in range(0,subsetsCount):
			temp = []
			for j in range(0,size):
				if ( i >> j) % 2 == 1:
					temp.append(S[j])
			result.append(temp)
		return result

s = Solution()
print s.subsets([0])
		
					        
