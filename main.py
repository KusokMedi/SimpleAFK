import pyautogui as gui
import random as r
import time as t

chill = {}
print("Bot Running in background. Close this window to stop programm.\n")
seconds = int(input("Enter a number (In Secconds) >>> "))
print(f"Your mouse are moving every {seconds}. Have fun at AFK!")


while True:
    x = r.randint(50,1200)
    y = r.randint(50,600)
    gui.moveTo(x,y,0.5)
    print(f"Moved to x={x}, y={y}.")
    t.sleep(seconds)
