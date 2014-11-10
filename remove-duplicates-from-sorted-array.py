class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		size = len(A)
		i = 0
		good = 0
		while i < size:
			curent = A[i]
			nexti = i + 1
			if nexti == size:
				
				A[good] = A[i]
				good = good + 1
				break
			else:
				next = A[nexti]
				if(curent == next):
					i = i + 1
				else:
					A[good] = A[i]
					good = good + 1
					i = i + 1

		A = A[0:good]

			
		return good  


s = Solution()
a = [1,1,2,3]
print s.removeDuplicates(a)
print a

