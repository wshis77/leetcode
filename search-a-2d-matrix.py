class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		row = len(matrix)
		if row == 0:
			return False
		start = 0
		end = row-1
		while end >  start + 1:
			mid = (start + end) / 2
			#print "mid" , mid
			if matrix[mid][0] == target:
				return True
			if matrix[mid][0] > target:
				end = mid
			else:
				start = mid
		currentrow = None
		if matrix[end][0] <= target:
			currentrow = matrix[end]
		else:
			currentrow = matrix[start]
		start = 0
		end = len(currentrow) - 1
		while end > start + 1:
			mid = (start + end) / 2
			if currentrow[mid] == target:
				return True
			if currentrow[mid] > target:
				end = mid
			else:
				start = mid
		if currentrow[start] == target or  currentrow[end] == target :
			return True
		return False


s = Solution()
#print s.searchMatrix([ [1,3,4,5,6],[7,9,11,23,45],[50,51,52,53,54],[100,111,112,113,114]],55)
print s.searchMatrix([[1],[3]],1)
