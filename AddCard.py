from ttkthemes import themed_tk as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from add_card import *
from check_table import *


class AddCard:
    def __init__(self, win):
        self.lbl1 = ttk.Label(win, text="Tier: ")
        self.lbl2 = ttk.Label(win, text="Name: ")
        self.lbl3 = ttk.Label(win, text="Level: ")
        self.lbl4 = ttk.Label(win, text="M/F: ")
        self.lbl5 = ttk.Label(win, text="POW: ")
        self.lbl6 = ttk.Label(win, text="TGH: ")
        self.lbl7 = ttk.Label(win, text="SPD: ")
        self.lbl8 = ttk.Label(win, text="CHA: ")
        self.lbl9 = ttk.Label(win, text="1st Proc: ")
        self.lbl10 = ttk.Label(win, text="2nd Proc: ")
        self.lbl11 = ttk.Label(win, text="Proc Amount: ")
        self.lbl12 = ttk.Label(win, text="U/D/L/R")

        self.t1 = ttk.Entry()
        self.t2 = ttk.Entry()
        self.t3 = ttk.Entry()
        v0 = IntVar()
        v0.set(1)
        self.r1 = ttk.Radiobutton(win, text="M", variable=v0, value=1)
        self.r2 = ttk.Radiobutton(win, text="F", variable=v0, value=2)
        self.t4 = ttk.Entry()
        self.t5 = ttk.Entry()
        self.t6 = ttk.Entry()
        self.t7 = ttk.Entry()
        v1 = IntVar()
        v1.set(1)
        self.r3 = ttk.Radiobutton(win, text="POW", variable=v1, value=1)
        self.r4 = ttk.Radiobutton(win, text="TGH", variable=v1, value=2)
        self.r5 = ttk.Radiobutton(win, text="SPD", variable=v1, value=3)
        self.r6 = ttk.Radiobutton(win, text="CHA", variable=v1, value=4)
        v2 = IntVar()
        v2.set(2)
        self.r7 = ttk.Radiobutton(win, text="POW", variable=v2, value=1)
        self.r8 = ttk.Radiobutton(win, text="TGH", variable=v2, value=2)
        self.r9 = ttk.Radiobutton(win, text="SPD", variable=v2, value=3)
        self.r10 = ttk.Radiobutton(win, text="CHA", variable=v2, value=4)
        self.t8 = ttk.Entry()
        v3 = IntVar()
        v3.set(1)
        self.r11 = ttk.Radiobutton(win, text="U", variable=v3, value=1)
        self.r12 = ttk.Radiobutton(win, text="D", variable=v3, value=2)
        self.r13 = ttk.Radiobutton(win, text="L", variable=v3, value=3)
        self.r14 = ttk.Radiobutton(win, text="R", variable=v3, value=4)
        self.b1 = ttk.Button(win, text="Add Card", command= lambda: self.get_query(v0, v1, v2, v3))

        self.lbl1.place(x=50, y=25)
        self.t1.place(x=150, y=25)
        self.lbl2.place(x=50, y=50)
        self.t2.place(x=150, y=50)
        self.lbl3.place(x=50, y=75)
        self.t3.place(x=150, y=75)
        self.lbl4.place(x=50, y=100)
        self.r1.place(x=150, y=100)
        self.r2.place(x=200, y=100)
        self.lbl5.place(x=50, y=125)
        self.t4.place(x=150, y=125)
        self.lbl6.place(x=50, y=150)
        self.t5.place(x=150, y=150)
        self.lbl7.place(x=50, y=175)
        self.t6.place(x=150, y=175)
        self.lbl8.place(x=50, y=200)
        self.t7.place(x=150, y=200)
        self.lbl9.place(x=50, y=225)
        self.r3.place(x=150, y=225)
        self.r4.place(x=200, y=225)
        self.r5.place(x=250, y=225)
        self.r6.place(x=300, y=225)
        self.lbl10.place(x=50, y=250)
        self.r7.place(x=150, y=250)
        self.r8.place(x=200, y=250)
        self.r9.place(x=250, y=250)
        self.r10.place(x=300, y=250)
        self.lbl11.place(x=50, y=275)
        self.t8.place(x=150, y=275)
        self.lbl12.place(x=50, y=300)
        self.r11.place(x=150, y=300)
        self.r12.place(x=200, y=300)
        self.r13.place(x=250, y=300)
        self.r14.place(x=300, y=300)
        self.b1.place(x=150, y=325)

        print(f"{self.t1.get()}")

    def get_query(self, v0, v1, v2, v3):
        query = f"SELECT * FROM {self.t1.get().lower()}_card WHERE name = '{self.t2.get()}' AND level = {self.t3.get()}"
        exist = check_table(query)

        if exist:
            messagebox.showerror("Error", "The card already exists.")
        else:
            if v0.get() == 1:
                gender = 'M'
            else:
                gender = 'F'

            if v1.get() == 1:
                proc_1 = 'POW'
            elif v1.get() == 2:
                proc_1 = 'TGH'
            elif v1.get() == 3:
                proc_1 = 'SPD'
            else:
                proc_1 = 'CHA'

            if v2.get() == 1:
                proc_2 = 'POW'
            elif v2.get() == 2:
                proc_2 = 'TGH'
            elif v2.get() == 3:
                proc_2 = 'SPD'
            else:
                proc_2 = 'CHA'

            if v3.get() == 1:
                arrow = 'U'
            elif v3.get() == 2:
                arrow = 'D'
            elif v3.get() == 3:
                arrow = 'L'
            else:
                arrow = 'R'

            query = f"INSERT INTO {self.t1.get().lower()}_card VALUES (" \
                    f"\"{self.t2.get()}\", " \
                    f"{self.t3.get()}, " \
                    f"'{gender}', " \
                    f"{self.t4.get()}, " \
                    f"{self.t5.get()}, " \
                    f"{self.t6.get()}, " \
                    f"{self.t7.get()}, " \
                    f"'{proc_1}', " \
                    f"'{proc_2}', " \
                    f"{self.t8.get()}, " \
                    f"'{arrow}')"

            add_card(query)
