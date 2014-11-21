class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		for i in range(0,9):
			check = {}
			for j in range(0,9):
				current = board[i][j]
				if current != ".":
					if check.has_key(current):
						return False
					else:
						check[current] = 1
		for i in range(0,9):
			check = {}
			for j in range(0,9):
				current = board[j][i]
				if current != ".":
					if check.has_key(current):
						return False
					else:
						check[current] = 1
		for i in range(0,3):
			for j in range(0,3):
				check = {}
				for ii in range(i*3,i*3+3):
					for jj in range(j*3,j*3+3):
						current = board[ii][jj]
						if current != ".":
							if check.has_key(current):
								return False
							else:
								check[current] = 1
		return True
	

		
		

					

