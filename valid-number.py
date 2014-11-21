class Solution:
    # @param s, a string
	# @return a boolean
	def isNumber(self, s):
		size = len(s)
		i = 0
		state = 0
		while i < size:
			current = s[i]
			print state,current,i,size
			if state == 0:
				if current == "+" or current == "-":
					state = 1
					i = i+ 1
				else:
					state = 1
			elif state == 1:
				if current.isdigit():
					state = 2
					i = i + 1
				elif current == ".":
					state = 3
					i = i + 1
				else:
					break
			elif state == 2:
				if current.isdigit():
					state = 2
					i = i + 1
				elif current == '.':
					state = 3
					i = i + 1
				else:
					state = 4
			elif state ==3:
				state = 4
			elif state == 4:
				if current.isdigit():
					state = 4
					i = i + 1
				if current == "e" or current == "E":
					state = 5
					i = i + 1
				else:
					break
			elif state == 5:
				if current == "+" or current == "-":
					state = 6
					i = i + 1
				else:
					state = 6
			elif state == 6:
				if current.isdigit():
					state = 7
					i = i + 1
				else:
					break
			elif state == 7:
				if current.isdigit():
					state = 7
					i = i + 1
				else:
					break
		#print "result", state, i , size
		if state == 3 and len(s) == 1:
			return False
		if i == size and( state == 2 or state == 4 or state == 7):
			return True
		else:
			return False
				




s = Solution()
print s.isNumber("1233.")
