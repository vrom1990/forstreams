'''
Запускаем firefox и ищем в нём то, что спросил пользователь
'''

import time
import pyautogui
import keyboard

pyautogui.press("win")
time.sleep(1)
pyautogui.write("paint")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(861, 535)
pyautogui.dragTo(861, 735, button='left')
pyautogui.dragTo(1061, 735, button='left')
pyautogui.dragTo(1061, 535, button='left')
pyautogui.dragTo(861, 535, button='left')
pyautogui.dragTo(961, 435, button='left')
pyautogui.dragTo(1061, 535, button='left')


