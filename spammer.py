import pyautogui, time  #pip install pyautogui
time.sleep(10)
f = open("spam", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
