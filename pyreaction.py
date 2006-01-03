#!/usr/bin/env python

from textgame import *
from player import *

import sys

VERSION = "0.01"

print "__"
print "|| Reaction v" + VERSION
print
print "Copyright (C) 2005-2006 Chris Porter."

g = TextGame()
g.start_game(5, 5, [Player(1), Player(2)])
