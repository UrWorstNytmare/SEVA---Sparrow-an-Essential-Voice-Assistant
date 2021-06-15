import pyautogui
import time

def increase_volume():
    i = 0
    while i < 5:
        pyautogui.press("volumeup")
        i = i + 1

def decrease_volume():
    i = 0
    while i < 5:
        pyautogui.press("volumedown")
        i = i + 1

def switch_window():
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    pyautogui.keyUp('alt')

def restore_down():
    pyautogui.keyDown('win')
    pyautogui.press('down')
    pyautogui.keyUp('win')

def minimize_window():
    pyautogui.keyDown('win')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.keyUp('win')

def maximize_window():
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')

def copy():
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

def cut():
    pyautogui.keyDown('ctrl')
    pyautogui.press('x')
    pyautogui.keyUp('ctrl')

def paste():
    pyautogui.keyDown('ctrl')
    pyautogui.press('v')
    pyautogui.keyUp('ctrl')

def select_all():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')

def save():
    pyautogui.keyDown('ctrl')
    pyautogui.press('s')
    pyautogui.keyUp('ctrl')

def save_as():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('s')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')

def close_current_program():
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

def open_settings():
    pyautogui.keyDown('win')
    pyautogui.press('i')
    pyautogui.keyUp('win')
