import RPi.GPIO as GPIO

class PIR:
    def __init__(self, pin, name, callback):
        self.pin = pin
        self.name = name

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=self.fired, bouncetime = 1000)
        self.callback = callback

    def fired(self, channel):
        self.callback(self.name);
