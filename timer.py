import pygame
import time
from datetime import datetime


pygame.init()
alarm_sfx = "alarm.wav"


desired_timerhrs = input("Enter hours: ")
desired_timermins = input("Enter minutes: ")
desired_timersecs = input("Enter seconds: ")
timerhrs = int(desired_timerhrs)
timermins = int(desired_timermins)
timersecs = int(desired_timersecs)
timerhrs = timerhrs * 3600
timermins = timermins * 60

t = timerhrs + timermins + timersecs


def countdown(t:int):
    while t > 0:
        print (f"Time left: {t}")
        time.sleep(1)
        t -= 1
    if t == 0:
        pygame.mixer.init()
        pygame.mixer.music.load(alarm_sfx)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print ("Timer is done")


countdown(t)
