import os
import keyboard
import pyautogui

# Change these values to match your specific application and keybind
APP_NAME = "HITMAN3.exe"
KEYBIND = "CTRL + ALT + Q"

# Get the PID of the application
output = os.popen("tasklist /fi \"imagename eq {}\" /fo csv /nh".format(APP_NAME)).read()
pid = int(output.strip().split(",")[1].replace('"', ''))

# Define the callback function
def force_quit():
    os.kill(pid, 9)
    pyautogui.alert("Application force quit successfully.")

# Register the keybind
keyboard.add_hotkey(KEYBIND, force_quit)

# Keep the script running
keyboard.wait()