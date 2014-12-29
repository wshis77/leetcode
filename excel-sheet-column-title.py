class Solution:
    # @return a string
    def convertToTitle(self, num):
		result = ""
		alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXY"
		while num > 0:
			temp = num % 26
			result = alpha[temp] + result
			num = num / 26
			if temp == 0 :
				num = num - 1 
		return result

s = Solution()
for i in range(1,55):
	print i,s.convertToTitle(i)
print s.convertToTitle(26*26*26)
			
        

