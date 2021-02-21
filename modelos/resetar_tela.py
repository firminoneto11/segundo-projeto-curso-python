from pynput.keyboard import Key, Controller
from os import system


def clear_terminal():
    system('cls')
    print('')


def clear_pycharm():
    """
    Essa função limpa a tela do terminal do PyCharm
    :return: None
    """
    keyboard = Controller()
    tecla = Key.f5
    # with keyboard.pressed(Key.alt):
    #    keyboard.press("'")
    keyboard.press(tecla)
    keyboard.release(tecla)
    clear_terminal()
