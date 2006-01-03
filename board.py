from square import *

class Board:
  def __init__(self, parent, width, height, players):
    self.parent = parent
    self.width = width
    self.height = height
    self.board = []
    self.winner = False
    self.players = players
    self.currentplayer = players[0]
    
    for x in range(0, width):
      b = []
      for y in range(0, height):
        b.append(Square(self, x, y))
      
      self.board.append(b)
      
    self.on_boardchange()
    
  def on_boardchange(self):
    # virtual
    pass

  def move(self, x, y, depth = 0):
    if depth > self.width * self.height * 50:
      raise AssertionError("too much recursion") #winner code goes ere
    
    if x < 0 or x >= self.width or y < 0 or y >= self.height:
      return False
    
    b = self.board[x][y]
    
    if depth == 0 and b.player and b.player != self.currentplayer:
      return False

    max = 5
    
    if x == 0 or x == self.width - 1:
      max = max - 1

    if y == 0 or y == self.height - 1:
      max = max - 1
      
    b.player = self.currentplayer
    b.count = b.count + 1
    if b.count == max:
      b.count = 1
      coords = [[1, 0], [0, 1], [-1, 0], [0, -1]];
      for c in coords:
        self.move(x + c[0], y + c[1], depth + 1)
        
    if depth == 0:
      self.on_boardchange()      
      self.next_player()
    
    return True
  
  def next_player(self):
    # this needs to be improved
    index = self.players.index(self.currentplayer)
    index = (index + 1) % len(self.players)
    self.currentplayer = self.players[index]
    