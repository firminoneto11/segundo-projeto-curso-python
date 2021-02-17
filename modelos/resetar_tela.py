from pynput.keyboard import Key, Controller


def clear_pycharm():
    """
    Essa função limpa a tela do terminal do PyCharm
    :return: None
    """
    keyboard = Controller()
    tecla = Key.f10
    # with keyboard.pressed(Key.alt):
    #    keyboard.press("'")
    keyboard.press(tecla)
    keyboard.release(tecla)
