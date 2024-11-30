# 021 Faça um progrma em Python que abra e reproduza o áudio de um arquivo MP3

import pygame
# Pygame é uma biblioteca usada em jogos 
# Usamos apenas para tocar musica

pygame.init()
# Inicia o pygame
pygame.mixer.music.load('Nome do arquivo.mp3')
# Mostra o que deve tocar
pygame.mixer.music.play()
# Toca o arquivo
pygame.event.wait()
# Espera a musica acabar para encerrar o programa