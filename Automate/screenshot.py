import pyautogui
import time
def capture():
        random = time.time()
        img = pyautogui.screenshot()
        img.save("C:\\Users\\Yuvraj Sharma\\Pictures\\" + str(random) + ".jpg")