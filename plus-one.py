class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		if len(digits) == 0:
			return digits
		positive = True
		if(digits[0] == "-"):
			positive = False
			digits = digits[1:]
		if(digits[0] == "+"):
			digits = digits[1:]
		if positive:
			carry = 1 
			size = len(digits)
			i = size-1
			while carry > 0 and i >= 0:
				value = digits[i]
				value = value + carry
				if( value >= 10):
					carry = 1
					value = 0
				else:
					carry = 0
				digits[i] = value
				i = i - 1
			if carry != 0:
				digits.insert(0,1)
		else:
			if len(digits) == 1 and digits[0] == 0:
				return [1]
			if len(digits) == 1 and digits[0] == 1:
				return [0]
			carry = 1
			size = len(digits)
			i = size - 1
			while carry > 0 and i >=0:
				value = digits[i]
				value = value - carry
				if value < 0:
					carry = 1
					value = 9
				else:
					carry = 0
				digits[i] = value
				i = i-1
			while digits[0] == 0 and len(digits) > 1:
				digits.remove(0)
			digits.insert(0,'-')
		return digits

s = Solution()
print s.plusOne([ 1,0,0,0])



