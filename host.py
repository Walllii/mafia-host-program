# Walli's project
from tkinter import *
from datetime import datetime

root = Tk()
root.title('Mafia Host')
root.iconphoto(True, PhotoImage(file='C:\\Users\\KDFX Modes\\Desktop\\mafia_host\\ved_icon.png'))
root.resizable(width=False, height=False)
root.configure(bg='#1f3f3f')

temp = 0
after_id = ''
num_player = int


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%S')
    label1.configure(text=str(f_temp))
    temp += 1
    if f_temp > '49':
        label1['bg'] = 'red'
    elif f_temp < '50':
        label1['bg'] = '#040069'

    if f_temp == '59':
        label1['text'] = 'S T O P'
        label1['fg'] = 'red'
        label1['bg'] = '#040069'
        stop_sw()


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
    label1.configure(bg='#040069', fg='white')
    tick()


def reset_sw():
    global temp
    temp = 0
    label1.configure(text='00', bg='#040069', fg='white')
    btn3.grid_forget()
    btn4.grid_forget()
    btn1.grid(row=1, columnspan=2, sticky='ew')


label1 = Label(root, width=6, font=('DS-Digital', 30), text='00',
               background='#040069', foreground='white')

label1.grid(row=0, columnspan=2, sticky='ew')

btn1 = Button(root, text='S t a r t',
              font=('Impact Light', 10),
              border='4',
              bg='#A19999',
              command=start_sw)

btn2 = Button(root,
              text='Stop',
              font=('Impact Light', 10),
              border='4',
              bg='#A19999',
              command=stop_sw)

btn3 = Button(root,
              text='Start',
              font=('Impact Light', 10),
              border='4',
              bg='#A19999',
              command=continue_sw)

btn4 = Button(root,
              text='Reset',
              font=('Impact Light', 10),
              border='4',
              bg='#A19999',
              command=reset_sw)

btn1.grid(row=1, columnspan=2, sticky='ew')

root.option_add("*tearOff", FALSE)


# ==============================================#

def delete_fols():
    global counter
    counter = [0 for i in range(10)]
    labels_folls = [Label_foll(i + 1) for i in range(10)]


def ppk_enable():
    if show_roles['state'] == 'disabled':
        show_roles.configure(state='normal')
        show_roles.configure(bg='#A19999')
    else:
        show_roles.configure(state='disabled')
        show_roles.configure(bg='#7a7979')


main_menu = Menu()
file_menu = Menu()
file_menu.add_cascade(label='Delete_fols', command=delete_fols)
main_menu.add_cascade(label="Option", menu=file_menu)

timer_menu = Menu()
timer_menu.add_checkbutton(label='Turn on', command=ppk_enable)
main_menu.add_cascade(label="ППК", menu=timer_menu)

root.config(menu=timer_menu)
root.config(menu=file_menu)
root.config(menu=main_menu)


# ==============================================#


player_counters = ['red' for i in range(10)]


class Players_Button:

    def __init__(self, x):
        self.x = Button(root, text=f'{x}',
                        font=('Impact Light', 20, 'bold'),
                        border='4',
                        foreground=player_counters[x - 1],
                        background='#A19999',
                        command=self.button_kill
                        )

        if x <= 5:
            self.x.grid(row=2, column=x - 1, sticky='ew')
        elif x > 5:
            self.x.grid(row=3, column=x - 6, sticky='ew')

        column_size = [0, 1, 2, 3, 4]
        for i in column_size:
            root.grid_columnconfigure(i, minsize=120)

    def button_kill(self):
        if self.x['foreground'] == 'red':
            self.x['foreground'] = '#757A80'
            self.x['background'] = '#403E39'

        elif self.x['foreground'] == '#757A80':
            self.x['foreground'] = 'red'
            self.x['background'] = '#A19999'


player_buttons = [Players_Button(i + 1) for i in range(10)]

# ===============================================

counter = [0 for i in range(10)]


class Label_foll():

    def __init__(self, y):

        self = Label(
            root,
            font=('Impact Light', 23,),
            text=f'{counter[y - 1]}',
            width=1,
            height=1,
            anchor=CENTER,
            bg='#1f3f3f',
            fg='white',
        )

        if y <= 5:
            self.grid(row=2, column=y - 1, sticky='ne', pady=8, padx=8)
        else:
            self.grid(row=3, column=y - 6, sticky='ne', pady=8, padx=8)


labels_folls = [Label_foll(i + 1) for i in range(10)]


def edit_foll(y, sign):
    global counter
    if sign == '+' and -1 < counter[y - 1] < 4:
        counter[y - 1] += 1
    elif sign == '-' and 0 < counter[y - 1] < 5:
        counter[y - 1] -= 1
    labels_folls[y - 1] = Label_foll(y)


class Buttons_foll:

    def __init__(self, y, sign):
        self.sign = sign
        self.y = Button(root, text=f"{y} {sign}", width=1, bg='#A19999', border='4', foreground='blue',
                        command=lambda: edit_foll(y, sign))
        if self.sign == '+':
            if y % 2 == 1:
                self.y.grid(row=4, column=(y // 2), ipadx=20, sticky='w')
            else:
                self.y.grid(row=4, column=(y // 2) - 1, ipadx=20, sticky='e')
        if self.sign == '-':
            if y % 2 == 1:
                self.y.grid(row=5, column=(y // 2), ipadx=20, sticky='w')
            else:
                self.y.grid(row=5, column=(y // 2) - 1, ipadx=20, sticky='e')


folls_add = [Buttons_foll(i + 1, "+") for i in range(10)]
folls_remove = [Buttons_foll(i + 1, "-") for i in range(10)]


# ===============================================

def delete_text():
    enter.delete(0, 'end')


def new_game():
    global counter, player_counters
    player_counters = ['red' for i in range(10)]
    counter = [0 for i in range(10)]
    enter_roles.delete(0, 'end')
    enter.delete(0, 'end')
    player_buttons = [Players_Button(i + 1) for i in range(10)]
    labels_folls = [Label_foll(i + 1) for i in range(10)]


roles = str()


def show():
    global roles, player_counters
    if enter_roles.get().isdigit() and len(enter_roles.get()) == 4:
        roles = enter_roles.get()
        print(type(roles))
        enter.delete(0, 'end')
        enter.insert(0, roles)
    for i in range(10):
        if i + 1 == int(roles[0]):
            player_counters[i] = 'yellow'
            player_buttons[i] = Players_Button(i + 1)
        elif i + 1 == int(roles[1]):
            player_counters[i] = 'purple'
            player_buttons[i] = Players_Button(i + 1)
        elif i + 1 == int(roles[2]) or i + 1 == int(roles[3]):
            player_counters[i] = 'black'
            player_buttons[i] = Players_Button(i + 1)
        else:
            player_buttons[i] = Players_Button(i + 1)


enter = Entry(root, width=8, background='#A19999', foreground='#305200', borderwidth=5, font=('DS-Digital', 20))
enter.grid(row=0, column=2, columnspan=2, sticky='news')
delete = Button(root,
                text='Delete',
                font=('Impact Light', 10),
                anchor=CENTER,
                border='4',
                bg='#A19999',
                command=delete_text
                )

enter_roles = Entry(root, width=2, font=('TNR', 10), background='#A19999', borderwidth=5, highlightbackground='red',
                    foreground='black', show='*')

show_roles = Button(root,
                    text='П П К',
                    font=('Impact Light', 10, 'bold'),
                    border='4',
                    bg='#7a7979',
                    activebackground='red',
                    state='disabled',
                    command=show
                    )

NEW = Button(root,
             text='N E W',
             font=('Impact bold', 10),
             foreground='#03961B',
             activebackground='green',
             border='4',
             bg='#A19999',
             command=new_game
             )

delete.grid(row=1, column=2, sticky='we')
enter_roles.grid(row=1, column=3, sticky='news')
show_roles.grid(row=1, column=4, sticky='news')
NEW.grid(row=0, column=4, sticky='news')


root.mainloop()
