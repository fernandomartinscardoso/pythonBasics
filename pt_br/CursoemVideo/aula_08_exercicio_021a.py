import pygame
pygame.mixer.init()
pygame.mixer.music.load('samplemusic01.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
