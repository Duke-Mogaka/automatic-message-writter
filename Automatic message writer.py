import pyautogui as pyt
import time

# inputs field
limit = input("Enter number of messages:")
message = input("Enter message:")

i = 0
time.sleep(5)
while i < int(limit):
    pyt.typewrite(message)
    pyt.press('Enter')  # start writing the messages on pressing enter key
    i += 1

