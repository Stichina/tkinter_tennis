from tkinter import *
import random

wind = Tk()
wind.geometry('601x386')
wind.resizable(False, False)

def KeyPress(event):
	global KS, KW, KU, KD
	if event.keycode == 40:
		KD = True
	if event.keycode == 38:
		KU = True
	if event.keycode == 83:
		KW = True
	if event.keycode == 87:
		KS = True
	print(event.keycode)


def KeyRelease(event):
	global KS, KW, KU, KD
	if event.keycode == 40:
		KD = False
	if event.keycode == 38:
		KU = False
	if event.keycode == 83:
		KW = False
	if event.keycode == 87:
		KS = False
def Timer():
	canvas.itemconfig(img_na_pole, image=field_image)
	buttonstart.place_forget()
	name1.place_forget()
	name2.place_forget()
	rPvsP.place_forget()
	rCvsC.place_forget()
	rPvsC.place_forget()
	Labelreg.place_forget()

	name11 = name1.get()
	name22 = name2.get()
	Labelname1.configure(text=name11)
	Labelname2.configure(text=name22)
	Labelname1.place(x=100, y=20)
	Labelname2.place(x=400, y=20)
	hpp.configure(text='поздравляю, победил ' + name11)
	hpp2.configure(text='поздравляю, победил ' + name22)

	global KS, KW, KU, KD, p1x, p1y, p2x, p2y, PlayerX, PlayerY, b_vx, b_vy, ball_x, ball_y, cy, cx
	canvas.itemconfig(ball, state='normal')
	canvas.itemconfig(PlayerY, state='normal')
	canvas.itemconfig(PlayerX, state='normal')

	res.place(x=270, y=20)
	bexit.place(x=10, y=10)

	ball_x = b_vx + ball_x
	ball_y = b_vy + ball_y
	if ball_y < 0:
		b_vy = 3
	if ball_y > 386:
		b_vy = -3

	if ball_x < p1x + 26 and ball_y < p1y + 100 and ball_y > p1y:
		b_vx = 3

	if ball_x > p2x and ball_y < p2y + 100 and ball_y > p2y:
		b_vx = -3

	if ball_x < 0:
		b_vx = 3
		cy += 1
		res.configure(text=str(cx) + ' : ' + str(cy))
	if ball_x > 601:
		b_vx = -3
		cx += 1
		res.configure(text=str(cx) + ' : ' + str(cy))

	if KU == True:
		p2y -= 2
		if p2y < 0:
			p2y = 0
	if KD == True:
		p2y += 2
		if p2y > 386 - 112:
			p2y = 386 - 112
	if KS == True:
		p1y -= 2
		if p1y < 0:
			p1y = 0
	if KW == True:
		p1y += 2
		if p1y > 386 - 112:
			p1y = 386 - 112

	if cy == 5:
		b_vx = 0
		b_vy = 0
		ball_x = 0
		ball_y = 0
		hpp.place(x=200, y=30)

	if cx == 5:
		b_vx = 0
		b_vy = 0
		ball_x = 0
		ball_y = 0
		hpp2.place(x=200, y=30)
	canvas.coords(ball, ball_x, ball_y)
	canvas.coords(PlayerY, p1x, p1y)
	canvas.coords(PlayerX, p2x, p2y)
	wind.after(5, Timer)

def CandMe():
	canvas.itemconfig(img_na_pole, image=field_image)
	buttonstart.place_forget()
	name1.place_forget()
	name2.place_forget()
	rPvsP.place_forget()
	rCvsC.place_forget()
	rPvsC.place_forget()
	Labelreg.place_forget()

	name11 = name1.get()
	name22 = name2.get()
	Labelname1.configure(text=name11)
	Labelname2.configure(text=name22)
	Labelname1.place(x=100, y=20)
	Labelname2.place(x=400, y=20)
	hpp.configure(text='поздравляю, победил ' + name11)
	hpp2.configure(text='поздравляю, победил ' + name22)

	global KS, KW, p1x, p1y, p2x, p2y, PlayerX, PlayerY, b_vx, b_vy, ball_x, ball_y, cy, cx
	canvas.itemconfig(ball, state='normal')
	canvas.itemconfig(PlayerY, state='normal')
	canvas.itemconfig(PlayerX, state='normal')

	res.place(x=270, y=20)
	bexit.place(x=10, y=10)

	ball_x = b_vx + ball_x
	ball_y = b_vy + ball_y
	if ball_y < 0:
		b_vy = 3
	if ball_y > 386:
		b_vy = -3

	if ball_x < p1x + 26 and ball_y < p1y + 100 and ball_y > p1y:
		b_vx = 3

	if ball_x > p2x and ball_y < p2y + 100 and ball_y > p2y:
		p2x=ball_x
		p2y=ball_y
		b_vx = -3

	if ball_x < 0:
		b_vx = 3
		cy += 1
		res.configure(text=str(cx) + ' : ' + str(cy))
	if ball_x > 601:
		b_vx = -3
		cx += 1
		res.configure(text=str(cx) + ' : ' + str(cy))

	if KS == True:
		p1y -= 2
		if p1y < 0:
			p1y = 0
	if KW == True:
		p1y += 2
		if p1y > 386 - 112:
			p1y = 386 - 112

	if cy == 5:
		b_vx = 0
		b_vy = 0
		ball_x = 0
		ball_y = 0
		hpp.place(x=200, y=30)

	if cx == 5:
		b_vx = 0
		b_vy = 0
		ball_x = 0
		ball_y = 0
		hpp2.place(x=200, y=30)

	canvas.coords(ball, ball_x, ball_y)
	canvas.coords(PlayerY, p1x, p1y)
	canvas.coords(PlayerX, p2x, p2y)
	wind.after(5, Timer)

def vibor():
	if val.get()==0:
		buttonstart.configure(command=Timer)
	if val.get()==1:
		buttonstart.configure(command=CandMe)
	if val.get()==2:
		buttonstart.configure(command=Timer)
wind.bind('<KeyPress>', KeyPress)
wind.bind('<KeyRelease>', KeyRelease)

canvas = Canvas(width=601, height=384)
canvas.pack()
field_image = PhotoImage(file='pole.gif')
menu_image = PhotoImage(file='menu.gif')
img_na_pole = canvas.create_image(0, 0, image=menu_image, anchor='nw')

p1x = 0
p1y = 384 / 2 - 112 / 2
p2x = 601 - 24
p2y = 384 / 2 - 112 / 2

PlayerY_image = PhotoImage(file='p2.gif')
PlayerY = canvas.create_image(p1x, p1y, image=PlayerY_image, anchor='nw', state='hidden')

PlayerX_image = PhotoImage(file='p1.gif')
PlayerX = canvas.create_image(p2x, p2y, image=PlayerX_image, anchor='nw', state='hidden')

ball_x = 601 // 2
ball_y = 384 // 2
b_vx = random.randint(0, 1)
b_vy = random.randint(0, 1)
if b_vx == 0:
	b_vx = 3
else:
	b_vx = -3
if b_vy == 0:
	b_vy = 3
else:
	b_vy = -3

ball_image = PhotoImage(file='ball.gif')
ball = canvas.create_image(ball_x, ball_y, image=ball_image, anchor='center', state='hidden')

cx = 0
cy = 0
res = Label(text=str(cx) + ' : ' + str(cy), font=('Times New Roman', '15'), fg='black', bg='white')

bexit = Button(text='exit', bg='red', command=exit)
bexit.place(x=300, y=200)

'''cong_image = PhotoImage(file='flowers.gif')
cong = Label(image=cong_image)'''

Labelreg = Label(text='режим игры')
Labelreg.place(x=50, y=159)

val = IntVar()

rPvsP = Radiobutton(text='Человек вис человек', value=0, variable=val, command=vibor)
rPvsP.place(x=50, y=183)

rPvsC = Radiobutton(text='Человек вис компухтер', value=1, variable=val, command=vibor)
rPvsC.place(x=50, y=213)

rCvsC = Radiobutton(text='Копухтер вис компухтер', value=2, variable=val, command=vibor)
rCvsC.place(x=50, y=240)

buttonstart=Button(text='start', bg='lightgreen')
buttonstart.place(x=300, y=170)

name1 = Entry()
name2 = Entry()
name1.place(x=70, y=10)
name2.place(x=360, y=10)
name1.insert(0, 'введите имя игрока 1')
name2.insert(0, 'введите имя игрока 2')

Labelname1 = Label(text=name1, bg='pink')
Labelname2 = Label(text=name2, bg='pink')

hpp = Label(bg='yellow')
hpp2 = Label(bg='yellow')

KS = False
KW = False
KD = False
KU = False


wind.mainloop()

