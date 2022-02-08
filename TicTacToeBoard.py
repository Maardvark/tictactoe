#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
class Board:
	def __init__(self):
		self.boardList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
		print(self)
		self.winConditions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
		#self.winConditions.append([0,1,2], [3,4,5], [6,7,8]) #horizontal wins
		#self.winConditions.append([0,3,6], [1,4,7], [2,5,8]) #vertical wins
		
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
		new_list = []
		for value in self.boardList:
			try:
				new_list.append(int(value))
				return False
			except ValueError:
				continue
				
		return True
		
#newBoard = Board() #testing