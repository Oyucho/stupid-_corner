# import pyautogui as auto
# import time

#while True:
    ##auto.press('entger')
    #time.sleep(1)

import pyautogui as auto  # Importing the pyautogui module as 'auto' for simulating keyboard and mouse actions
import time  # Importing the time module to add delays

# Function to send a message repeatedly
def send_message():
    try:
        while True:
            auto.write("You online?")  # Type the message "You online?"
            auto.press('enter')  # Press the 'Enter' key to send the message
            time.sleep(1)  # Wait for 1 second before repeating the action
    except KeyboardInterrupt:
        print("Program terminated by user.")  # Handle manual interruption (Ctrl+C) by the user
    except Exception as e:
        print(f"An error occurred: {e}")  # Catch and print any other exceptions

# Main entry point of the script
if __name__ == "__main__":
    send_message()  # Call the send_message function to start the message sending loop