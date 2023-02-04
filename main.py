import time
import pyautogui
import keyboard

import sys


def refresh():
    # Click Refresh button
    print("Refreshing shop...")
    refreshCoordinates = None
    while refreshCoordinates is None:
        refreshCoordinates = pyautogui.locateCenterOnScreen("refresh_button.PNG")
    pyautogui.click(refreshCoordinates)
    time.sleep(0.2)


def confirm():
    # Click Confirm button button
    print("Confirming refresh...")
    confirmCoordinates = None
    while confirmCoordinates is None:
        confirmCoordinates = pyautogui.locateCenterOnScreen("confirm_button.png")
    pyautogui.click(confirmCoordinates)
    time.sleep(1)


def findCovenantBookmarks():
    # Find Covenant Bookmarks
    print("Searching for Covenant Bookmarks...")
    covenantCoordinates = None
    covenantCoordinates = pyautogui.locateCenterOnScreen("covenant_bookmarks.png", confidence=0.8)
    if covenantCoordinates is None:
        print("Bookmarks not found...")
    else:
        pyautogui.moveTo(covenantCoordinates)
        pyautogui.click(pyautogui.position().x + 800, pyautogui.position().y + 30)
        time.sleep(0.2)
        pyautogui.click(pyautogui.locateCenterOnScreen("purchase_covenant_bookmark.png"))
        time.sleep(1)


def findMysticMedals():
    # Find Mystic Medals
    print("Searching for Mystic Medals...")
    mysticCoordinates = None
    mysticCoordinates = pyautogui.locateCenterOnScreen("mystic_medals.png", confidence=0.8)
    if mysticCoordinates is None:
        print("Medals not found...")
    else:
        pyautogui.moveTo(mysticCoordinates)
        pyautogui.click(pyautogui.position().x + 800, pyautogui.position().y + 30)
        time.sleep(0.2)
        pyautogui.click(pyautogui.locateCenterOnScreen("purchase_mystic_medals.png"))
        time.sleep(1)


def scrollShop():
    print("Scrolling...")
    pyautogui.scroll(-3)
    time.sleep(1)


def purchase():
    skystones = input("Skystones: ")
    possible_refreshes = int(int(skystones) / 3)
    print("Number of refreshes: " + str(possible_refreshes))
    while True:
        if keyboard.is_pressed("r"):
            for x in range(possible_refreshes):
                refresh()
                confirm()
                findCovenantBookmarks()
                findMysticMedals()
                scrollShop()
                findCovenantBookmarks()
                findMysticMedals()
                print("Cycle finished...")
                print("-----------------")
            print("-----------------")
            print("Finished...")
        if keyboard.is_pressed("e"):
            print("Exiting....")
            sys.exit()


if __name__ == "__main__":
    print("R to start\n"
          "E to exit\n"
          "Application can NOT be stopped while running! If you need to stop press WIN + D, this fails image search "
          "and you can close the app in IDE!")
    purchase()
