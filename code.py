#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: March 2022
# This is a space aliens game.

import random
import stage
import time
import ugame

import constants


def splash_scene():
    # this function is the splash_scene
    
    # get sound ready
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    
    # sets the background to image 0
    # and the size (10x8 titels of the size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    
    
     # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    # create a stage
    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layter of all sprites to show up in order
    game.layers = [background]
    # render all sprites
    # most likely will only render background once per game scnece
    game.render_block()

    # repeat forever, game loop
    while True:
        # wait for 2 seconds
        time.sleep(2.0)
        menu_scene()

        #redraw Sprites
        game.tick()

def menu_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    
    # add text objects
    
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette =constants.RED_PALETTE, 
    buffer = None)
    text1.move(20, 10)
    text1.text("MT Game Studios!")
    text.append(text1)
    
    text2 = stage.Text(width=29, height=12, font=None, palette =constants.RED_PALETTE, 
    buffer = None)
    text2.move(40, 110)
    text2.text("PRESS START!")
    text.append(text2)
    # sets the background to image 0
    # and the size (10x8 titels of the size 16x16)
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    # create a stage
    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layter of all sprites to show up in order
    game.layers = text + [background]
    # render all sprites
    # most likely will only render background once per game scnece
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        #redraw Sprites
        game.tick()


def game_scene():
    # this function is the main game game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    
    # buttons that you want to keep information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    
    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    # sets the background to image 0
    # and the size (10x8 titels of the size 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_X, 
                            constants.SCREEN_Y)
    
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.radiant(1, 3)
            background.tile(x_location, y_location, tile_picked)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    
    alien = stage.Sprite(image_bank_sprites,9 ,
    int (constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 
    16)

    # create a stage
    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layter of all sprites to show up in order
    game.layers = [ship] + [alien] + [background]
    # render all sprites
    # most likely will only render background once per game scnece
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # a button
        if keys & ugame.K_O != 0:
           if a_button == constants.button_state["button_up"]:
            a_button = constants.button_state["button_just_pressed"]
           elif a_button == constants.button_state["button_just_pressed"]:
            a_button = constants.button_state["button_still_pressed"]
            
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else: 
                a_button = constants.button_state["button_up"]
            # B button
        if keys & ugame.K_X:
            print("B")
        if keys & ugame.K_START:
            print("Start")
        if keys & ugame.K_SELECT:
            print("Select")
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

        if keys & ugame.K_UP != 0:
            pass
        if keys & ugame.K_DOWN != 0:
            pass

        # update game logic
        # play sound ig A was just button_just_pressed
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)
        # redraw Sprites
        game.render_sprites([ship] + [alien])
        game.tick()

if __name__ == "__main__":
    splash_scene()
