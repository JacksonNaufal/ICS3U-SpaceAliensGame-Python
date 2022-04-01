#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a "Hello, World! program, tested for space aliens.


import stage
import ugame


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    
    # sets the bacgrkound to image 0 
    # and the size (10x8 titels of the size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)


    # create a stage
    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layter of all sprites to show up in order
    game.layers = [background]
    # render all sprites
    # most likely will only render background once per game scnece
    game.render_block()


    # repeat forever, game loop
    while True:
        pass  # just a placeholder for now

if __name__ == "__main__":
    game_scene()
