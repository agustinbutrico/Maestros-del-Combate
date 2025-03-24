import os, random
import data.game_state as gs
import ui.messages as uim
from time import sleep

def limpiar_pantalla():
    if os.name == 'nt':  # Windows
        print()
        os.system('cls')
    else:  # Linux, macOS, etc.
        print()
        os.system('clear')

def time_battle_end(): # time
    sleep(2)