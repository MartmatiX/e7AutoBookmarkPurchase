# e7AutoBookmarkPurchase
This application uses image recognition in Python and searches for Covenant Bookmarks and Mystic Medals in the Secret Shop.

# Prerequisites
  1. Python
  2. IDE of your choice (PyCharm recommended)
  3. pip -> Pillow and SimpleCV
  4. pyautogui, keyboard, time, sys libraries (can be imported in IDE)
  5. Epic Seven on PC running in emulator (preferably Bluestacks)
  
# Requirements
  1. Import project
  2. Create screenshots of Secret Shop and name them:

    a. Refresh button - refresh_button.PNG
    b. Dialog confirm button - confirm_button.png
    c. Covenant bookmarkS - covenant_bookmarks.png
    d. Buy button of Covenant Bookmarks - purchase_covenant_bookmark.png
    e. Mystic Medal - mystic_medals.png
    f. Buy button of Mystic Medals - purchase_mystic_medals.png
  3. Upload those images to the project folder - this is required because pyautogui library is looking for exact pixel match in the image
  * examples can be found in the project folder
  * Bluestacks has to run in the resolution you took the screenshots in, otherwise the image recognition will not work
  
# Usage
  1. Open project in IDE
  2. Start application
  3. Enter number of Skystones you want to spend and confirm with Enter
  4. Open Epic Seven with Secret Shop already opened
  5. Press R on keyboard
  6. Wait until the programm finishes
  * If you want to exit the program before it finishes, minimize Bluestacks. This will halt the image recognition and you can kill the program in the IDE.
  7. While the application is running it will print action that is currently happening
  8. Your mouse will be moving automatically to the buttons, so don't get scared someone hacked you :)
  
# Disclaimers
  1. This project is not in finished state, therefore there is no executable file
  2. If everything is set up correctly the program should not miss any bookmarks, but to be sure run a few test cycles before you put thousands of skystones in
  3. In the slowest scenario the program takes 30 minutes to process 1000 Skystones
  4. I don't know if I will return to this project so you can do whatever you want with the source files, but please credit me, just to make me happy :)
