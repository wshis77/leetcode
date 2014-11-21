class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		if x == 0 or x == 1:
			return x
		start = x / 2
		end = 1
		while start > end:
			#print start,end
			if start == end + 1:
				break
			mid = (start + end) / 2
			
			nn = mid*mid
			if nn == x:
				return mid
			elif nn > x:
				start = mid 
			else:
				end = mid
		if start*start <= x:
			return start
		else:
			return end





s = Solution()
print s.sqrt(1)
print s.sqrt(2)
print s.sqrt(3)
print s.sqrt(4)
print s.sqrt(5)
print s.sqrt(6)
print s.sqrt(7)
print s.sqrt(8)
print s.sqrt(9)
print s.sqrt(10)
					        
