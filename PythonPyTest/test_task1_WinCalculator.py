# Import the relevant packages
import os
import time
import pyautogui
import win32con
import win32gui
import win32clipboard


def test_win():
    # Starting the test by loading calculator app
    os.system("calc.exe")
    time.sleep(1)

    # maximize the calculator app
    maxi = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(maxi, win32con.SW_MAXIMIZE)

    # Run the test by sending keystrokes
    pyautogui.press("5")
    time.sleep(0.5)
    pyautogui.press("+")
    time.sleep(0.5)
    pyautogui.press("5")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)

    pyautogui.doubleClick(pyautogui.position(1550, 165))
    pyautogui.hotkey('ctrl', 'c')
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    time.sleep(1.5)

    # Assert the result
    assert data == '10'

    # Test cleanup - close the calculator
    os.system("TASKKILL /F /IM Calculator.exe")

    print("This is the value", data)

    # Print message as report
    print("calculator has been closed")

