from Tkinter import *
from tkboard import *
from game import *

class TkGameForm(Frame):
  def push(self, x, y):
    self.parent.board.move(x, y)
    
  def curry(self, x, y):
    return lambda: self.push(x, y)
  
  def createwidgets(self):
    for x in range(0, self.bwidth):
      na = []
      for y in range(0, self.bheight):
        newb = Button(self)
        newb["command"] = self.curry(x, y)
        
        newb.grid(row = y, column = x, rowspan = 1, columnspan = 1, sticky = N+E+S+W)
        na.append(newb)
        
      self.buttons.append(na)

  def __init__(self, parent, master, width, height):
    Frame.__init__(self, master)
    self.parent = parent
    
    top = self.winfo_toplevel()
    top.rowconfigure(0, weight = 1)
    top.columnconfigure(0, weight = 1)
    
    for x in range(0, width):
      self.columnconfigure(x, weight = 1, minsize = 50)
    for y in range(0, height):
      self.rowconfigure(y, weight = 1, minsize = 50)
    
    self.buttons = []
    self.bwidth = width
    self.bheight = height
    self.grid(sticky = N+E+S+W)
    self.createwidgets()
    
class TkGame(Game):
  def __init__(self):
    Game.__init__(self, TkBoard)
    self.root = Tk()
    self.root.title("PyReaction")
    
  def start_game(self, width, height, players):
    self.form = TkGameForm(self, self.root, width, height)
    Game.start_game(self, width, height, players)
    self.form.mainloop()
    try:
      self.root.destroy()
    except TclError:
      pass
    
  