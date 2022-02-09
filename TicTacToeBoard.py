#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
class Board:
	def __init__(self):
		self.boardList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		print(self)
		
		self.rows = {1:[0,1,2], 2:[3,4,5], 3:[6,7,8]}
		self.columns = {1:[0,3,6], 2:[1,4,7], 3:[2,5,8]}
		self.diagonals = {1:[0,4,8], 2:{2,4,6]}
		#[0,1,2], [3,4,5], [6,7,8] #horizontal wins
		#[0,3,6], [1,4,7], [2,5,8] #vertical wins
		#[0,4,8], [2,4,6] diagonal wins
		self.winConditions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
		
	def __str__(self):
		boardString = ""
		spaceCount = 1 #counting 1, 2, 3 to find position to add \n
		for spaceIndex in range(9): #9 = number of spaces
			boardString = boardString + str(self.boardList[spaceIndex])
			
			if spaceCount == 3:
				boardString += "\n"
				spaceCount = 1
				continue
			else:
				boardString += "|"
				
			spaceCount += 1	
		
		return boardString
		
	def hasWinner(self):
		for winCondition in self.winConditions:
			if self.boardList[winCondition[0]] == self.boardList[winCondition[1]] == self.boardList[winCondition[2]]:
				return True
		
		return False
		
	def isBoardFull(self):
		tempList = []
		for value in self.boardList:
			try:
				tempList.append(int(value)) #if a single entry can be cast to an int, then that means at least one space on the board is still open
				return False
			except ValueError:
				continue
				
		return True #if all spaces are taken, then there will be no integers in self.boardList...if we get this far without a winner, then we have a draw
		
#newBoard = Board() #testing