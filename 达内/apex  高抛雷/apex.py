import win32gui
import time


def draw():
    hwin = win32gui.GetDesktopWindow()
    hwindc = win32gui.GetWindowDC(hwin)

    while True:
        for i in range(-2,2):
            for c in range(-2,2):
                win32gui.SetPixel(hwindc,960+i,540+c,0x0000FF)

        for i in range(-9,9):
            for c in range(-1,1):
                win32gui.SetPixel(hwindc,960+i,700+c,0x0000FF)
                win32gui.SetPixel(hwindc,960+i,750+c,0x0000FF)
                win32gui.SetPixel(hwindc,960+i,796+c,0x0000FF)
                win32gui.SetPixel(hwindc,960+i,815+c,0x0000FF)

        time.sleep(0.01)

    win32gui.ReleaseDC(hwin, hwindc)


try:
    draw()
except:
    print("error")

