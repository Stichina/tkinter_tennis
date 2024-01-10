
import tkinter as tk

count=0 #счет для кнопки стоп

x=0 #счет игрока1
y=0 #счет игрока2

ball_x=1000//2   #координаты мяча по х
ball_y=514//2    #координаты мяча по у
ball_vx=4   #скорость мяча по х
ball_vy=5   #скорость мяча по у

racket_left_x=5
racket_left_y=514//2

racket_right_x=985
racket_right_y=514//2


def stop():
    global ball_x, ball_y, ball_vx, ball_vy, count
    if count == 0:
        buttonstop.configure(bg='green', text='replay')
        ball_vx=0
        ball_vy=0
        count=1
    else:
        buttonstop.configure(bg='red', text='stop')
        count=0
        ball_vx = 4
        ball_vy = 5

def restart():
    global ball_vx, ball_vy, x, y, ball_y, ball_x
    ball_x = 1000 // 2
    ball_y = 514 // 2

def physics():
    global ball_vx, ball_vy, x, y, ball_y, ball_x
    label.place(x=950 // 2, y=15, w=100, h=50)
    buttonstop.place(x=100, y=30)
    buttonend.place(x=15, y=80)
    buttonrestart.place(x=15, y=30)
    buttonstart.place_forget()
    buttonexit.place_forget()
    canvas2.place_forget()
    ball_x+=ball_vx
    ball_y+=ball_vy
    canvas.coords(ball,ball_x,ball_y)
    label.configure(text='счет: '+str(x)+':'+ str(y))
    
    if ball_x<=0+20 or ball_x>=980:
        
        label.configure(text='вы проиграли\n'
                             'счет: '+str(x)+':'+ str(y))
   
    
    if ball_y>=514-21 or ball_y<=0+20:
        ball_vy=-ball_vy
        
    if ball_y<racket_left_y+56 and ball_y>racket_left_y-56: #112 - высота ракетки
        if ball_x<racket_left_x+26 and ball_x>racket_left_x:
            ball_vx=-ball_vx #мяч отразился
            x+=1
            label.configure(text='счет: '+str(x)+':'+str(y))
            
    if ball_y<racket_right_y+56 and ball_y>racket_right_y-56: #112 - высота ракетки
        if ball_x<racket_right_x+26 and ball_x>racket_right_x-26:
            ball_vx=-ball_vx #мяч отразился
            y+=1
            label.configure(text='счет: '+str(x)+':'+ str(y))
    
    canvas.coords(ball,ball_x,ball_y)        
    
    window.after(25, physics)
    
def keycodeevent(event):
    global racket_left_x, racket_left_y,racket_right_x, racket_right_y
    print(event)
    if event.keycode == 83:
        racket_left_y+=35
    if event.keycode==87:
        racket_left_y-=35    
    canvas.coords(racket_left,racket_left_x,racket_left_y)
    
    if event.keycode == 40:
        racket_right_y+=35
    if event.keycode==38:
        racket_right_y-=35    
    canvas.coords(racket_right,racket_right_x,racket_right_y)    
    

window=tk.Tk()
window.geometry('1000x514')

canvas=tk.Canvas()
canvas.place(x=0, y = 0, w=1000, h=514)

canvas2=tk.Canvas()
canvas2.place(x=0, y=0, w=1000, h=514)

field_image = tk.PhotoImage(file ='field2.gif' )
field=canvas.create_image(0, 0, anchor='nw', image=field_image)

kot_image=tk.PhotoImage(file='fon.gif')
kot=canvas2.create_image(0, -300, anchor='nw',image=kot_image)

ball_image=tk.PhotoImage(file = 'ball.gif')
ball=canvas.create_image(ball_x, ball_y, anchor='center', image=ball_image)

racket_left_image=tk.PhotoImage(file='p2.gif')
racket_left=canvas.create_image(racket_left_x, racket_left_y, anchor='w', image=racket_left_image)

racket_right_image=tk.PhotoImage(file='p1.gif')
racket_right=canvas.create_image(racket_right_x, racket_right_y, anchor='e', image=racket_right_image)
window.bind('<Key>', keycodeevent)

label=tk.Label(bg='white', text='счет  '+ str(y)+':'+str(x), font='Arial 11', anchor='center')

buttonrestart=tk.Button(text='Restart', bg='orange', font='Arial 15',anchor='center', command=restart)

buttonstop=tk.Button(text='stop', bg='red', command=stop)

buttonend=tk.Button(bg='lightblue', text='end', command=exit)

buttonstart=tk.Button(bg='yellow', text='start', font='Arial 20', command=physics)
buttonstart.place( x=950//2, y=514//2 )

buttonexit=tk.Button(bg='lightgreen', text='exit', font='Arial 20', command=exit)
buttonexit.place( x=950//2, y=514//2+70 )

window.mainloop()

