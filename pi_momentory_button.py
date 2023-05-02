import RPi.GPIO as GPIO
import time


def button(pin_number):
    GPIO.setmode(GPIO.BCM)

    # Setup GPIO pins
    button_pin = pin_number
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        # Read button state
        button_state = GPIO.input(button_pin)

        # When the button is pressed, it's false******
        if not button_state:
            # print("Button pressed")
            time.sleep(0.2)  # Debounce delay
            return true
