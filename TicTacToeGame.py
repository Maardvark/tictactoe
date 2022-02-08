from TicTacToeBoard import Board

class Game:
	def __init__(self):
		self.board = Board()
		self.startGameLoop()
		
	def startGameLoop(self):
		playerPieces = ["x", "o"]
		playerIndex = 0
		
		while not self.board.isBoardFull():
			selectSpace = input("Select space to place piece: ")
			
			if selectSpace in self.board.boardList:
				self.board.boardList[int(selectSpace) - 1] = playerPieces[playerIndex]
				playerIndex = self.switchPlayer(playerIndex)
				print(self.board)
			else:
				print("Invalid entry. Try again.\n")
				
			if self.board.hasWinner():
				print("WINNER")
				break
		
		print("GAME OVER")
	
	def switchPlayer(self, playerIndex):
		if playerIndex == 0:
			return 1
		else:
			return 0
		
newGame = Game() #testing