#!/usr/bin/env python

from player import *

import sys, getopt

VERSION = "0.01"

underline = ""
for i in range(0, len(VERSION)):
  underline = underline + "="

print "__"
print "|| Reaction v" + VERSION
print "=============" + underline
print
print "Copyright (C) 2005-2006 Chris Porter."

def usage():
  import os
  print 
  print "Usage: %s [OPTION]" % os.path.basename(sys.argv[0])
  print
  print "Arguments:"
  print
  print "-d, --dimensions=     Set board dimensions (default 5x5)."
  print "-h, --help            This help screen."
  print "-p, --players=        Set number of players, from 2 to 9 (default 2)."
  print "-t, --text-mode       Text mode (default false)."
  
textmode = False
players = 2
width = 5
height = 5

try:
  opts, args = getopt.getopt(sys.argv[1:], "thp:d:", ["text-mode", "help", "players=", "dimensions="])
except getopt.GetoptError:
  usage()
  sys.exit(1)
  
for o, a in opts:
  if o in ("-h", "--help"):
    usage()
    sys.exit(1)
  if o in ("-t", "--text-mode"):
    textmode = True
  if o in ("-p", "--players"):
    players = int(a)
    if players < 2 or players > 9:
      print
      print "Warning: players must be greater than 1 and less than 10."
      usage()
      sys.exit(1)
  if o in ("-d", "--dimensions"):
    import re
    m = re.match("^([2-9])x([2-9])$", a)

    if not m:
      print
      print "Warning: dimensions must be of the form wxh, both must be at least 2 and at most 9.";
      usage()
      sys.exit(1)
    
    width = int(m.group(1))
    height = int(m.group(2))
    
    
if players * 2 > width * height:
  print
  print "You must have at least two squares per player."
  usage()
  sys.exit(1)
  
p = []
for i in range(0, players):
  p.append(Player(i + 1))

if textmode:
  import textgame
  g = textgame.TextGame()
else:
  import tkgame
  g = tkgame.TkGame()

print
print "Board size: %dx%d" % (width, height)
print "Players: %d" % players
if textmode:
  print "Text mode: yes"
else:
  print "Text mode: no"
print
print "Game started."

g.start_game(width, height, p)

print "Game completed."