from game import *
from textboard import *

class TextGame(Game):
  def __init__(self):
    Game.__init__(self, TextBoard)

  def start_game(self, width, height, players):
    Game.start_game(self, width, height, players)
    
    while not self.board.winner:
      import re
    
      pmove = raw_input("Player %d (%s) -- enter move: " % (self.board.currentplayer.number, pieces[self.board.currentplayer.number]))
      
      out = re.match("^([A-Za-z])(\d+)$", pmove)
      if out:
        column = out.group(1)
        row = out.group(2)
      else:
        out = re.match("^(\d+)([A-Za-z])$", pmove)
        if not out:
          print "Invalid selection."
          continue
        
        row = out.group(1)
        column = out.group(2)
              
      row = int(row)
      
      if row < 1 or row > self.board.height:
        print "Invalid selection."
        continue
      
      column = ord(str.upper(column)) - ord('A') + 1
      
      if column > self.board.width:
        print "Invalid selection."
        continue
                     
      if not self.board.move(column - 1, row - 1):
        print "Move failed."
        
    print "Player %d (%s) wins!" % (b.winner.number, pieces[b.winner.number])
    