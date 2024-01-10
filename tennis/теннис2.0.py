from tkinter import *
import random

gor = 601
vert = 384
wind = Tk()
wind.geometry('601x384')
wind.resizable(False, False)

KS = False
KW = False
KD = False
KU = False

def KeyPress(event):
    global KS, KW, KU, KD
    if event.keycode == 40:
        KD = True
    if event.keycode == 38:
        KU = True
    if event.keycode == 87:
        KW = True
    if event.keycode == 83:
        KS = True


def KeyRelease(event):
    global KS, KW, KU, KD
    if event.keycode == 40:
        KD = False
    if event.keycode == 38:
        KU = False
    if event.keycode == 87:
        KW = False
    if event.keycode == 83:
        KS = False

class Rocket:
    def __init__(self, ex, ey, image):
        self.x = ex
        self.y = ey
        self.img=image

    def image(self):
        canvas.create_image(self.x, self.y, image=self.image, anchor='nw', state='hidden')

    def move_right(self):
        if KU == True:
            self.y -= 2
            if self.y < 0:
                p2y = 0
        if KD == True:
            self.y += 2
            if self.y > 386 - 112:
                self.y = 386 - 112

    def move_left(self):
        if KS == True:
            self.y -= 2
            if self.y < 0:
                self.y = 0
        if KW == True:
            self.y += 2
            if self.y > 386 - 112:
                self.y = 386 - 112

class Ball:
    def __init__(self, ex, ey, image):
        self.x = ex
        self.y = ey
        self.img=image
        self.speed=3

    def image(self):
        canvas.create_image(self.x, self.y, image=self.image, anchor='nw', state='hidden')

    def move(self):
        ball_x = self.x + self.speed
        ball_y = self.y + self.speed
        if ball_y < 0:
            self.speed = 3
        if ball_y > 386:
            self.speed= -3

        if self.x > right_rocket.x or self.y == right_rocket.y:
            self.speed = -3

        if self.x < left_rocket.x or self.y == left_rocket.y:
            self.speed = 3

canvas = Canvas(width=601, height=384)
canvas.pack()
field_image = PhotoImage(file='pole.gif')
menu_image = PhotoImage(file='menu.gif')
img_na_pole = canvas.create_image(0, 0, image=field_image, anchor='nw')

rr_image=PhotoImage(file='p2.gif')
right_rocket = Rocket(0, vert // 2 + 12, rr_image)
right_rocket.move_right()
right_rocket.image()

lr_image=PhotoImage(file='p2.gif')
left_rocket = Rocket(gor, vert // 2 + 12, lr_image)
left_rocket.move_right()
left_rocket.image()
vibor=[0, gor]
ball_image=PhotoImage('ball.gif')
ball=Ball(random.choice(vibor), vert // 2 + 12, ball_image)
wind.mainloop()
