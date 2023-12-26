import pyautogui
import time

# Give yourself a few seconds to switch to the screen where you want the script to work
time.sleep(5)

# Open 'Run' dialog box (Win + R)
pyautogui.hotkey('win', 'r')

# Wait for the 'Run' dialog box to open
time.sleep(1)

# Type the path of the folder on your desktop
# Replace 'YourFolderName' with the actual name of your folder
pyautogui.typewrite(r'C:\Users\user\OneDrive\Desktop\qayyum_jazimin')

# Press 'Enter' to open the folder
pyautogui.press('enter')
