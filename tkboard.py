from board import *

pieces = ['*', 'X', '!', '/', '=', '?', '$', '@', '#']

class TkBoard(Board):
  def on_boardchange(self):
    Board.on_boardchange(self)
    b = self.parent.form.buttons
    for x in range(0, self.width):
      for y in range(0, self.height):
        square = self.board[x][y]
        if square.player:
          p = pieces[square.player.number - 1]
        
        if square.count == 0:
          v = "   \n   \n   "
        elif square.count == 1:
          v = "\n %s \n" % p
        elif square.count == 2:
          v = "%s  \n   \n  %s" % (p, p)
        elif square.count == 3:
          v = "%s  \n %s \n  %s" % (p, p, p)
        elif square.count == 4:
          v = "%s %s\n   \n%s %s" % (p, p, p, p)
        
        b[x][y]["text"] = v