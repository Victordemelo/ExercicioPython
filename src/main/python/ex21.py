# Objetivo: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Autor: Victor M

import pygame

pygame.init()

pygame.mixer.music.load('C:/Users/victor/Codigos_Programação/vscode/Python1/ExercicioPython/src/main/python/ex21.mp3')
pygame.mixer.music.play()
pygame.time.wait(180000)
