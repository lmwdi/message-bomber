import time
import keyboard
import pyautogui

    # sleep time for go to telegram
time.sleep(5)
    # message number
for i in range(1,500):
    # type your message
    keyboard.write("your text")
    # press enter and send message
    keyboard.press("Enter")