class Solution:
	def twoSum(self, num, target):
		size = len(num);
		for i in range(0,size):
			for j in range(i+1, size):
				if num[i] + num[j] == target:
					return (i+1,j+1)
				else:
					continue

s = Solution()
print(s.twoSum((2,7,11,15),9))
