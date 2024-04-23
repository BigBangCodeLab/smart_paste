import keyboard  # Library for detecting hotkey
import pyperclip  # Library for accessing clipboard
import pygame  # Library for playing sounds
import time  # Library for time operations

def play_typing_sound():
    # Initialize the pygame mixer if it's not already initialized
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    # Load the typing sound
    typing_sound = pygame.mixer.Sound("quick-mechanical-keyboard-14391.mp3")
    # Play the typing sound
    typing_sound.play(loops=-1)

def stop_typing_sound():
    # Stop the typing sound
    pygame.mixer.stop()

def type_text(text):
    for char in text:
        # Simulate typing each character
        keyboard.write(char)
        # Add a slight delay for realistic typing speed
        time.sleep(0.02)

def on_hotkey():
    # Get the text from the clipboard
    text = pyperclip.paste()
    # If there's any text in the clipboard
    if text:
        # Play typing sound
        play_typing_sound()
        # Simulate typing by writing the text
        type_text(text)
        # Stop typing sound
        stop_typing_sound()

if __name__ == "__main__":
    # Define your hotkey (Ctrl + Shift + Q)
    keyboard.add_hotkey("ctrl+shift+q", on_hotkey)

    # Start listening for the hotkey
    keyboard.wait()
