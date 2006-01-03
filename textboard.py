from board import *

pieces = ['*', 'X', '!', '/', '=', '?', '$', '@', '#']

class TextBoard(Board):
  def on_boardchange(self):
    Board.on_boardchange(self)
    
    print
    sdi = "  -"
    dout = "  "
    
    for i in range(0, self.width):
      dout = dout + "  %s  " % chr(ord('A') + i)
      sdi = sdi + "-----"
      
    print dout
    
    for y in range (0, self.height):
      dout = "%d " % (y + 1)
      dout2 = "  "
      
      print sdi
    
      for x in range (0, self.width):
        square = self.board[x][y]

        if square.count == 0:
          value = value2 = "  "
        else:
          p = pieces[square.player.number - 1]
          if square.count == 1:
            value = p + " "
            value2 = "  "
          elif square.count == 2:
            value = p + " "
            value2 = " " + p
          elif square.count == 3:
            value = p + p
            value2 = p + " "
          elif square.count == 4:
            value = value2 = p + p
                  
        dout = dout + "| %s " % value
        dout2 = dout2 + "| %s " % value2
      
      print dout + "|"
      print dout2 + "|"
      
    print sdi
    print

    