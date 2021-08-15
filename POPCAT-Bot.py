import pyautogui, time
import random as rd
pyautogui.FAILSAFE= True

time.sleep(5)
i = 1
while i>0:
    time.sleep(rd.triangular(0.01, 0.04, 0.014))
    pyautogui.press("space")
