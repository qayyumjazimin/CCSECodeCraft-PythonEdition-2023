import pyautogui
import time

# Function to type and search a query
def search_query(query):
    # Type the query
    pyautogui.typewrite(query)
    time.sleep(1)  # Wait for a second

    # Press 'Enter' to search
    pyautogui.press('enter')
    time.sleep(3)  # Wait for the search results to load

# Start the automation
time.sleep(5)  # Wait for you to switch to the browser

# Use 'Tab' to focus on the Google search bar
for _ in range(6):  # Adjust the number of times 'Tab' is pressed if necessary
    pyautogui.press('tab')
    time.sleep(0.5)

# Step 1: Search for "Big Bang Korea"
search_query("Big Bang Korea")

# Step 2: Navigate to Google Images
# This will still require finding the Google Images link
# Adjust the number of 'Tab' presses as needed
for _ in range(14):  # Adjust based on your browser layout
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('enter')
time.sleep(3)  # Wait for Google Images to load

# Step 3: Wait for 5 seconds
time.sleep(5)

# Step 4: Search for "Ahmad Qayyum Fikri"
# Assuming the focus is back on the search bar
for _ in range(4):  # Adjust based on your browser layout
    pyautogui.press('tab')
    time.sleep(0.5)
pyautogui.press('backspace')  # Clear the search bar
search_query("Ahmad Qayyum Fikri")
