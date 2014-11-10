class Solution:
	# @return a list of lists of integers
	def combine(self, n, k):
		result = []
		if(k == n):
			temp = []
			for i in range(1,n+1):
				temp.append(i)
			result.append(temp)
			return result
		result = []
		if(k == 1):
			for i in range(1,n+1):
				temp = [i]
				result.append(temp)
			return result
		result = []
		for i in range(1, n+1):
			if(i > k-1):
				temp = self.combine(i-1,k-1)
				print i-1 , k-1, temp
				temp2 = self.deepcopy(temp)
				print i-1 , k-1, temp2
				for t in temp2:
					result.append(t.append(i))
				
		return result

	def deepcopy(self,l):
		result = []
		for item in l:
			temp = []
			for t in item:
				temp.append(t)
			result.append(temp)
		return result

s = Solution()
print (s.combine(3,2))


			
