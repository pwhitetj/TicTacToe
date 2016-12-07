#!/usr/bin/python3

####
# generate a script that runs a bunch of tic tac toe games
####

xstart = 20
ystart = 20
xwidth = 310
ywidth = 350
for xc in range(6):
    for yc in range(3):
        print("python3 ttt.py %i %i random random &" % (xstart+xc*xwidth, ystart+yc*ywidth))
        
