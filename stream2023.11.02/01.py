'''
Открываем блокнот
пишем туда текст
сохраняем
'''

import time
import pyautogui
import keyboard

pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("del")
pyautogui.write("Hello!")
time.sleep(3)
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.press("enter")