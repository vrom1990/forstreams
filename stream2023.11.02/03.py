'''
Запускаем firefox и ищем в нём то, что спросил пользователь
'''

import time
import pyautogui
import keyboard

pyautogui.press("win")
time.sleep(1)
pyautogui.write("firefox")
time.sleep(1)
pyautogui.press("enter")
zapros = pyautogui.prompt(text='Введите текст запроса',
                 title='Введите текст запроса' ,
                 default='Зачем мне холодильник, если я не курю')
keyboard.write(zapros)
pyautogui.press("enter")