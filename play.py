import pygame
from Lemon import lemon
import os
midi_music = lemon()
music = midi_music.generator()
#混音器参数
freq = 44100
bit_size = -16
channels = 2
buffer = 2048
pygame.mixer.init(freq, bit_size, channels, buffer)
clock = pygame.time.Clock()
pygame.mixer.music.load("{}.MID".format(music))
pygame.mixer.music.play()
import turtle

turtle.speed(1)
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

turtle.write("庆", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()
turtle.write("祝", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

turtle.write("澳", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()

turtle.write("门", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

turtle.write("回", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(50, 0)
turtle.pendown()

turtle.write("归", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

turtle.write("24", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

turtle.write("周", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

turtle.write("年", font=("Arial", 36, "normal"))
turtle.penup()
turtle.goto(250, 0)
turtle.pendown()

turtle.done()

while pygame.mixer.music.get_busy():
    clock.tick(30)

# 程序结束后删除生成的临时MIDI文件
os.remove("{}.MID".format(music))