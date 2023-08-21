#faça um programa em python que abra e reproduza o audio de um arquivo mp3

import pygame

pygame.mixer.init()
nome_arquivo = "caminho/do/arquivo.mp3"  # Substitua pelo caminho do seu arquivo MP3
pygame.mixer.music.load("021.mp3")
pygame.mixer.music.play()

# Mantém o programa em execução enquanto o áudio está sendo reproduzido
while pygame.mixer.music.get_busy():
    continue




