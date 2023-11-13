'''
Открываем блокнот
спрашиваем название будущего файла
спрашиваем текст будущего файла
пишем туда текст
сохраняем под указанным именем
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
fileText = pyautogui.prompt(text='Введите текст',
                 title='Введите текст будущего файла' ,
                 default='Тут текст')
fileName = pyautogui.prompt(text='Введите заголовок',
                 title='Введите заголовок будущего файла' ,
                 default='Текстовый файл')
keyboard.write(fileText)
time.sleep(3)
pyautogui.hotkey("ctrl", "s")
time.sleep(1)

keyboard.write(fileName)
pyautogui.press("enter")
