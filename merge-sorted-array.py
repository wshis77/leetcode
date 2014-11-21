class Solution:
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		i = 0
		j = 0
		while i < len(A) and  j < len(B):
			print A,i,j,B
			while i < len(A) and A[i] <= B[j]:
				i = i + 1
			while j < len(B)and i < len(A) and A[i] > B[j]:
				A.insert(i,B[j])
				i = i + 1
				j = j + 1
		if(j < len(B)):
			while j < len(B):
				A.insert(len(A),B[j])
				j = j + 1

s = Solution()
a = []
s.merge(a,5,[1],4)
print a
