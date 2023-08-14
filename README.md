# Minesweeper for Thumby

This is written in Micropython. It is meant to be played on a Thumby or on a Thumby emulator, such as the one on https://code.thumby.us/.

It is a standard Minesweeper game on easy mode, i.e. there is a 10x10 grid and you must flag 10 mines to win.

Controls: Press A to select a square that you think is safe. Press B to place a flag on a square that you think is a mine.

Since the thumby screen is too small to accomodate a 10x10 grid, I made a 9x5 grid, with the ability to scroll down and across to view the whole board.