import pygame
import time
from datetime import datetime


pygame.init()
alarm_sfx = "alarm.wav"
pygame.mixer.init()

while True:                                 #so it keeps asking if input is invalid
    desiredtime = input("Enter time (H:M:S): ")


    try:                                        #checks for errors before runnning
        parts = desiredtime.split(":")          #takes each number between the :'s

        if len(parts) != 3:                     #makes sure there a 3 parts
            raise ValueError("Format must be H:M:S")

        hours, minutes, seconds = map(int, parts)
        t = hours * 3600 + minutes * 60 + seconds

        break                                   #breaks loop since valid input

    except ValueError:                          #If still doesn't work, exits cleanly
        print("Invalid format. Please enter time like 1:30:45 or 0:25:0")


def countdown(t:int):
    while t > 0:
        print (f"Time left: {t} seconds")
        time.sleep(1)
        t -= 1
    if t == 0:
        pygame.mixer.music.load(alarm_sfx)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print ("Timer is done")


countdown(t)
