import pyautogui as pag

import time
import os


def clicker(path: str, exp: str = '', sleep=1) -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__)) + '/' + exp
    time.sleep(sleep)
    btn = pag.locateOnScreen(base_dir + path, confidence=0.8)
    pag.click(btn)


if __name__ == '__main__':

    base_img = {
        'field': 'dark_msg_field.png',
        'send': 'dark_send.jpg',
        'smile': 'dark_smile.jpg',
    }

    # clicker(r'extension.jpg')

    dirname = 'base_img/'

    text = [
        'Hi',
        'Cool!',
    ]

    import random

    clicker(base_img.get('field'), dirname)
    time.sleep(1)
    pag.typewrite(random.choice(text))
    pag.typewrite('programmer!')
    time.sleep(1)
    clicker(base_img.get('smile'), dirname)
    clicker('images/programmer.jpg')
    clicker(base_img.get('send'), dirname)
