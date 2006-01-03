class Game:
  def __init__(self, boardclass):
    self.boardclass = boardclass
  
  def start_game(self, width, height, players):
    self.board = self.boardclass(width, height, players)
    