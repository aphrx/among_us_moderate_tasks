import pyautogui
import time
import numpy as np
from PIL import ImageGrab

def menu():
    print("What tasks would you like to do?")
    print("\nPart 1 Tasks")
    print("[0] Troubleshoot")
    print("[1] Submit Scan")
    print("[2] Download/Upload")
    print("[3] Accept Diverted Power/Stabilize Steering")
    print("[4] Empty Garbage")
    print("[5] Admin Swipe")
    print("[6] Fuel Engines")
    print("\nPart 2 Tasks")
    print("[7] Prime Shields")
    print("[8] Inspect Sample")
    print("[9] Align Engine")
    print("[10] Divert Power")
    print("[11] Fix Wires")
    print("[12] Calibrate Distributor")
    print("[13] Start Reactor")

    option = int(input("\noptions: "))

    if option == 0:
        troubleshoot()
    if option == 1:
        start_task()
        menu()
    if option == 2:
        start_task()
        download_upload()
        menu()
    if option == 3:
        start_task()
        accept_diverted_stabilize()
        menu()
    if option == 4:
        start_task()
        empty_garbage()
        menu()
    if option == 5:
        start_task()
        admin_swipe()
        menu()
    if option == 6:
        start_task()
        fuel_engines()
        menu()
    if option == 7:
        start_task()
        prime_shields()
        menu()
    if option == 8:
        start_task()
        inspect_sample()
        menu()
    if option == 9:
        start_task()
        align_engine_output()
        menu()
    if option == 10:
        start_task()
        divert_power()
        menu()
    if option == 11:
        start_task()
        fix_wires()
        menu()
    if option == 12:
        start_task()
        calibrate_distributor()
        menu()
    if option == 13:
        start_task()
        start_reactor()
        menu()


def troubleshoot():
    while True:
        print(pyautogui.position())

def start_task():
    pyautogui.moveTo(737, 549)
    pyautogui.click()
    time.sleep(0.5)

def download_upload():
    pyautogui.moveTo(414, 397)
    pyautogui.click()

def accept_diverted_stabilize():
    pyautogui.moveTo(401, 335)
    pyautogui.click()

def admin_swipe():
    pyautogui.moveTo(303, 483)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(157, 268)
    pyautogui.drag(600, 0, 0.8, button='left')

def empty_garbage():
    pyautogui.moveTo(576, 268)
    pyautogui.mouseDown()
    pyautogui.moveTo(576, 457)
    time.sleep(3)
    pyautogui.mouseUp()

def fuel_engines():
    pyautogui.moveTo(675, 515)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

def prime_shields():
    tiles = [(410, 230), (496, 271), (474, 389), (377, 441), (300, 383), (322, 273), (421, 330)]
    red = (202, 94, 112)
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for tile in tiles:
        if pix[tile] == red:
            pyautogui.moveTo(tile)
            pyautogui.click()

def inspect_sample():
    tubes = [(275, 360), (340, 360), (400, 360), (460, 360), (530, 360)]
    red = (246, 134, 134)
    pyautogui.moveTo(565, 554)
    pyautogui.click()
    time.sleep(70)
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for tube in tubes:
        if pix[tube] == red:
            pyautogui.moveTo(tube[0], 500)
            pyautogui.click()

def align_engine_output():
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    marker = (163, 163, 178)
    array = np.array(img)
    Y, X = np.where(np.all(array==marker, axis=2))
    pyautogui.moveTo(X[0], Y[0])
    pyautogui.mouseDown()
    pyautogui.moveTo(560, 330)
    pyautogui.mouseUp()

def divert_power():
    sliders = [(216, 471), (268, 471), (321, 471), (376, 471), (429, 471), (480, 471), (534, 471), (589, 471)]
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for slider in sliders:
        print(pix[slider])
        if pix[slider][0] > 150:
            pyautogui.moveTo(slider)
            pyautogui.mouseDown()
            pyautogui.moveTo(slider[0], 405)
            pyautogui.mouseUp()

def fix_wires():
    wires = [(182, 185), (182, 289), (182, 392), (182, 495), (610, 185), (610, 289), (610, 392), (610, 495)]
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for i in range(0, 4):
        for j in range(4, 8):
            if pix[wires[i]] == pix[wires[j]]:
                pyautogui.moveTo(wires[i])
                pyautogui.mouseDown()
                pyautogui.moveTo(wires[j])
                pyautogui.mouseUp()

def calibrate_distributor():
    distributor = [(315, 197), (315, 347), (315, 497)]
    marker = (71, 73, 71)
    buttons = [(555, 206), (549, 360), (557, 498)]
    for i in range(3):
        pyautogui.moveTo(buttons[i])
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 800, 630))
            pix = img.load()
            print(pix[distributor[i]])
            if pix[distributor[i]] == marker:
                pyautogui.click()
                break

def start_reactor():
    lights = [(153, 285), (230, 285), (307, 285), (148, 360), (232, 362), (310, 365), (148, 440), (232, 440), (310, 440)] 
    buttons = [(500, 285), (568, 285), (642, 285), (500, 360), (568, 362), (642, 365), (500, 440), (568, 440), (642, 440)] 
    on = (68, 168, 255)

    for i in range(5):
        flashed = []
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 800, 630))
            pix = img.load()
            for j in range(9):
                if(pix[lights[j]] == on):
                    flashed.append(j)
                    time.sleep(0.3)
            if len(flashed) == (i + 1):
                break
        
        time.sleep(0.5)
        print(flashed)
        for k in flashed:
            pyautogui.moveTo(buttons[k])
            pyautogui.click()
            time.sleep(0.2)

menu()
