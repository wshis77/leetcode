class MinStack:
	data = []
	minIndex = []
	def __init__(self):
		self.data = []
		self.minIndex = []
	# @param x, an integer
	# @return an integer
	def push(self, x):
		self.data.append(x)
		size = len(self.data)
		if size == 1:
			self.minIndex.append(0)
		else:
			min = self.data[self.minIndex[size-2]] 
			if min > x:
				self.minIndex.append(size-1)
			else:
				self.minIndex.append(self.minIndex[size-2])
		return x


	# @return nothing
	def pop(self):
		self.data.pop()
		self.minIndex.pop()
	# @return an integer
	def top(self):
		return self.data[len(self.data)-1]
	# @return an integer
	def getMin(self):
		min = None
		size = len(self.data)
		if size > 0:
			min = self.data[self.minIndex[size-1]]
		return min

m = MinStack()
m.push(1)
m.push(2)
m.push(-1)
m.push(-3)
m.push(5)
print m.getMin()
print m.data
print m.minIndex
