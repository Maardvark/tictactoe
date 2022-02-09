from TicTacToeBoard import Board

class Game:
	def __init__(self):
		self.board = Board()
		self.startGameLoop()
		
	def startGameLoop(self):
		playerPieces = ["x", "o"]
		playerIndex = 0
		
		#continue gameplay as long as the board is not full (game will also stop if someone wins)
		while not self.board.isBoardFull():
			selectSpace = input("Select space to place piece: ") #player select space (#1-9) to play piece
			
			#if a valid, available number is entered, the current player's piece will be placed on the selected space
			if selectSpace in self.board.boardList:
				self.board.boardList[int(selectSpace) - 1] = playerPieces[playerIndex] #set space to either "x" or "o"
				playerIndex = self.switchPlayer(playerIndex) #switch to next player (and switch to next piece)
				print(self.board)
			else:
				print("Invalid entry. Try again.\n") #only select available indices 1-9
				
			if self.board.hasWinner():
				print("GAME OVER - WINNER")
				return
		
		print("GAME OVER - DRAW")
	
	def switchPlayer(self, playerIndex):
		if playerIndex == 0:
			return 1
		else:
			return 0
		
newGame = Game() #testing