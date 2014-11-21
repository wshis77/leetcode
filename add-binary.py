class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		sizeA = len(a)
		sizeB = len(b)
		i = 0
		carry = 0
		result = []
 		while sizeA-1-i >= 0 and sizeB-1-i >= 0:
			acurrent = int(a[sizeA-1-i])
			bcurrent = int(b[sizeB-1-i])
			mysum = acurrent + bcurrent + carry
			carry = mysum / 2
			mysum = mysum % 2
			result.insert(0,str(mysum))
			i = i + 1
		if sizeA-1-i < 0 and sizeB-1-i < 0:
			if carry == 1:
				result.insert(0,"1")
		elif sizeA-1-i < 0:
			while sizeB-1-i >= 0:
				bcurrent = int(b[sizeB-1-i])
				mysum = bcurrent + carry
				carry = mysum / 2
				mysum = mysum % 2
				result.insert(0,str(mysum))
				i = i + 1
			if carry == 1:
				result.insert(0,"1")
		else:
			while sizeA-1-i >= 0:
				acurrent = int(a[sizeA-1-i])
				mysum = acurrent + carry
				carry = mysum / 2
				mysum = mysum % 2
				result.insert(0,str(mysum))
				i = i + 1
			if carry == 1:
				result.insert(0,"1")
		return "".join(result)
s = Solution()
print s.addBinary("1111111111111111111","1")
			

			


		

						        
