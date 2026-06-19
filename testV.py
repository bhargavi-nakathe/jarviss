import pyttsx3
import time

engine = pyttsx3.init()

for i in range(3):
    engine.say(f"This is test number {i+1}")
    engine.runAndWait()
    time.sleep(1)