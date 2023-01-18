from tkinter import *
from datetime import datetime
import math

# Walli's project

root = Tk()
root.title('Mafia Host')
root.resizable(width=False, height=False)
root.iconphoto(True, PhotoImage(file='/Users/a111/Desktop/hoster/mafia_hoster_logo.png'))
root.configure(bg='#1f3f3f')

temp = 0
after_id = ''
num_player = int


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1
    if f_temp > '00:49':
        label1['bg'] = 'red'
    elif f_temp < '00:50':
        label1['bg'] = '#040069'


def start_sw():
    btn1.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky='ew')
    tick()


def stop_sw():
    btn2.grid_forget()
    btn3.grid(row=1, column=0, sticky='ew')
    btn4.grid(row=1, column=1, sticky='ew')
    root.after_cancel(after_id)


def continue_sw():
    btn3.grid_forget()
    btn4.grid_forget()
    btn2.grid(row=1, columnspan=2, sticky='ew')
    tick()


def reset_sw():
    global temp
    temp = 0
    label1.configure(text='00:00', bg='#040069')
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky='ew')


label1 = Label(root,
               width=6,
               font=('DS-Digital', 50),
               text='00:00',
               background='#040069',
               foreground='white'
               )

label1.grid(row=0, columnspan=2, sticky='ew')

btn1 = Button(root, text='S t a r t',
              font=('Impact Light', 15),
              command=start_sw)

btn2 = Button(root,
              text='Stop',
              font=('Impact Light', 15),
              command=stop_sw)

btn3 = Button(root,
              text='Start',
              font=('Impact Light', 15),
              command=continue_sw)

btn4 = Button(root,
              text='Reset',
              font=('Impact Light', 15),
              command=reset_sw)

btn1.grid(row=1, columnspan=2, sticky='ew')


class Players_Button:

    def __init__(self, x):
        self.x = Button(root, text=f'{x}',
                        font=('Impact Light', 50, 'bold'),
                        border=3,
                        foreground='red',
                        command=self.button_kill
                        )

        if x <= 5:
            self.x.grid(row=2, column=x - 1, sticky='ew')
        elif x > 5:
            self.x.grid(row=3, column=x - 6, sticky='ew')

        column_size = [0, 1, 2, 3, 4]
        for i in column_size:
            root.grid_columnconfigure(i, minsize=100)

    def button_kill(self):
        if self.x['foreground'] == 'red':
            self.x['foreground'] = 'gray'
        elif self.x['foreground'] == 'gray':
            self.x['foreground'] = 'red'


player_buttons = [Players_Button(i + 1) for i in range(10)]

# ===============================================


counter = 0


class Label_foll:

    def __init__(self, y):

        self = Label(
            root,
            font=('Impact Light', 23,),
            text='0',
            width=1,
            height=1,
            anchor=CENTER,
            bg='#1f3f3f',
            fg='white'
        )

        if y <= 5:
            self.grid(
                row=2, column=y - 1, sticky='ne', pady=8, padx=8
            )
        elif y > 5:
            self.grid(
                row=3, column=y - 6, sticky='ne', pady=8, padx=8
            )


labels_folls = [Label_foll(i + 1) for i in range(10)]


class Buttons_foll:

    def __init__(self, y, sign):
        self.sign = sign
        self.y = Button(root, text=f"{y} {sign}", width=1, foreground='blue', command=Buttons_foll.add_foll(self))
        if self.sign == '+':
            if y % 2 == 1:
                self.y.grid(row=4, column=(y // 2), ipadx=3, sticky='w')
            else:
                self.y.grid(row=4, column=(y // 2) - 1, ipadx=3, sticky='e')
        if self.sign == '-':
            if y % 2 == 1:
                self.y.grid(row=5, column=(y // 2), ipadx=3, sticky='w')
            else:
                self.y.grid(row=5, column=(y // 2) - 1, ipadx=3, sticky='e')

    def add_foll(self):
        labels_folls[0].congigure(text='6')




foll1 = Buttons_foll(1, '+')
foll_1 = Buttons_foll(1, '-')
foll2 = Buttons_foll(2, '+')
foll_2 = Buttons_foll(2, '-')
foll3 = Buttons_foll(3, '+')
foll_3 = Buttons_foll(3, '-')
foll4 = Buttons_foll(4, '+')
foll_4 = Buttons_foll(4, '-')
foll5 = Buttons_foll(5, '+')
foll_5 = Buttons_foll(5, '-')
foll6 = Buttons_foll(6, '+')
foll_6 = Buttons_foll(6, '-')
foll7 = Buttons_foll(7, '+')
foll_7 = Buttons_foll(7, '-')
foll8 = Buttons_foll(8, '+')
foll_8 = Buttons_foll(8, '-')
foll9 = Buttons_foll(9, '+')
foll_9 = Buttons_foll(9, '-')
foll10 = Buttons_foll(10, '+')
foll_10 = Buttons_foll(10, '-')


# ===============================================

def delete_text():
    enter.delete(0, 'end')


def new_game():
    enter_roles.delete(0, 'end')
    enter.delete(0, 'end')


enter = Entry(root, background='#1f3f3f', foreground='#00FF34', font=('DS-Digital', 18))
enter.grid(row=0, column=2, columnspan=2, sticky='news')
delete = Button(root,
                text='Delete',
                font=('Impact Light', 15),
                anchor=CENTER,
                command=delete_text
                )

enter_roles = Entry(root, width=9, background='#1f3f3f', foreground='orange', show='# ')

show_roles = Button(root,
                    text='П П К',
                    font=('Impact Light', 15, 'bold'),
                    # command=show
                    )

NEW = Button(root,
             text='N E W',
             font=('Impact bold', 20),
             foreground='#03961B',
             activeforeground='red',
             command=new_game
             )

delete.grid(row=1, column=2, sticky='we')
enter_roles.grid(row=1, column=3, sticky='ew')
show_roles.grid(row=1, column=4, sticky='ew')
NEW.grid(row=0, column=4, sticky='news')

root.mainloop()
