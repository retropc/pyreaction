#!/usr/bin/env python

from textboard import *
from player import *

import sys

VERSION = "0.01"

print "__"
print "|| Reaction v" + VERSION
print
print "Copyright (C) 2005 Chris Porter."

p = [Player(1), Player(2)]
b = TextBoard(5, 5, p)

while not b.winner:
  import re
  
  
  pmove = raw_input("Player %d (%s) -- enter move: " % (b.currentplayer.number, pieces[b.currentplayer.number]))
  
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
  
  if row < 1 or row > b.height:
    print "Invalid selection."
    continue
  
  column = ord(str.upper(column)) - ord('A') + 1
  
  if column > b.width:
    print "Invalid selection."
    continue;
                 
  if not b.move(column - 1, row - 1):
    print "Move failed."
    
print "Player %d (%s) wins!" % (b.winner.number, pieces[b.winner.number])
  
