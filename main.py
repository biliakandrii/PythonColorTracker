import pyautogui
import time
import winsound

duration = 1000  # milliseconds
freq = 1000  # Hz
target_color = (55, 174, 108)

while True:
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    if px == target_color:
        winsound.Beep(freq, duration)
    time.sleep(5)

