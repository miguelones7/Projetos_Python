import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

#time.sleep(3)
#print(pyautogui.position())

pyautogui.click(x=750, y=1055)
time.sleep(2)
pyautogui.hotkey("win", "up")

pyautogui.click(x=23, y=270)
pyautogui.click(x=319, y=78)

time.sleep(10)
for i in range(7):
    pyautogui.press("tab")
    time.sleep(0.1)

time.sleep(0.5)
pyautogui.press("enter")
pyautogui.write("Oi, amor! Acabei de ligar o computador e estou enviando esta mensagem automaticamente.")
pyautogui.press("enter")




