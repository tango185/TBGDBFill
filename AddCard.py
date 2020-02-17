from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from add_card import *
from check_table import *


class AddCard:
    def __init__(self, win):
        self.lbl1 = ttk.Label(win, text="Tier: ")
        self.lbl2 = ttk.Label(win, text="Name: ")
        self.lbl3 = ttk.Label(win, text="M/F: ")
        self.lbl4 = ttk.Label(win, text="POW: ")
        self.lbl5 = ttk.Label(win, text="TGH: ")
        self.lbl6 = ttk.Label(win, text="SPD: ")
        self.lbl7 = ttk.Label(win, text="CHA: ")
        self.lbl8 = ttk.Label(win, text="1st Ability: ")
        self.lbl9 = ttk.Label(win, text="2nd Ability: ")
        self.lbl10 = ttk.Label(win, text="Arrow: ")

        self.t1 = ttk.Entry()
        self.t2 = ttk.Entry()
        self.v0 = IntVar()
        self.v0.set(1)
        self.r1 = ttk.Radiobutton(win, text="M", variable=self.v0, value=1)
        self.r2 = ttk.Radiobutton(win, text="F", variable=self.v0, value=2)
        self.t3 = ttk.Entry()
        self.t4 = ttk.Entry()
        self.t5 = ttk.Entry()
        self.t6 = ttk.Entry()
        self.v1 = IntVar()
        self.v1.set(1)
        self.r3 = ttk.Radiobutton(win, text="POW", variable=self.v1, value=1)
        self.r4 = ttk.Radiobutton(win, text="TGH", variable=self.v1, value=2)
        self.r5 = ttk.Radiobutton(win, text="SPD", variable=self.v1, value=3)
        self.r6 = ttk.Radiobutton(win, text="CHA", variable=self.v1, value=4)
        self.v2 = IntVar()
        self.v2.set(2)
        self.r7 = ttk.Radiobutton(win, text="POW", variable=self.v2, value=1)
        self.r8 = ttk.Radiobutton(win, text="TGH", variable=self.v2, value=2)
        self.r9 = ttk.Radiobutton(win, text="SPD", variable=self.v2, value=3)
        self.r10 = ttk.Radiobutton(win, text="CHA", variable=self.v2, value=4)
        self.v3 = IntVar()
        self.v3.set(1)
        self.r11 = ttk.Radiobutton(win, text="U", variable=self.v3, value=1)
        self.r12 = ttk.Radiobutton(win, text="D", variable=self.v3, value=2)
        self.r13 = ttk.Radiobutton(win, text="L", variable=self.v3, value=3)
        self.r14 = ttk.Radiobutton(win, text="R", variable=self.v3, value=4)
        # TODO Figure out the Enter button
        self.b1 = ttk.Button(win, text="Add Card", command=self.get_query)
        # TODO Add validation functionality

        self.lbl1.place(x=50, y=25)
        self.t1.place(x=150, y=25)
        self.lbl2.place(x=50, y=50)
        self.t2.place(x=150, y=50)
        self.lbl3.place(x=50, y=75)
        self.r1.place(x=150, y=75)
        self.r2.place(x=200, y=75)
        self.lbl4.place(x=50, y=100)
        self.t3.place(x=150, y=100)
        self.lbl5.place(x=50, y=125)
        self.t4.place(x=150, y=125)
        self.lbl6.place(x=50, y=150)
        self.t5.place(x=150, y=150)
        self.lbl7.place(x=50, y=175)
        self.t6.place(x=150, y=175)
        self.lbl8.place(x=50, y=200)
        self.r3.place(x=150, y=200)
        self.r4.place(x=200, y=200)
        self.r5.place(x=250, y=200)
        self.r6.place(x=300, y=200)
        self.lbl9.place(x=50, y=225)
        self.r7.place(x=150, y=225)
        self.r8.place(x=200, y=225)
        self.r9.place(x=250, y=225)
        self.r10.place(x=300, y=225)
        self.lbl10.place(x=50, y=250)
        self.r11.place(x=150, y=250)
        self.r12.place(x=200, y=250)
        self.r13.place(x=250, y=250)
        self.r14.place(x=300, y=250)
        self.b1.place(x=150, y=275)

        print(f"{self.t1.get()}")

    def get_query(self):
        if self.t1.get() == "" or self.t2.get() == "":
            messagebox.showwarning(None, "Tip: Enter Tier & Name to check if card exists.")
        elif self.t3.get() == "" and self.t4.get() == "" and self.t5.get() == "" and self.t6.get() == "":
            self.check_card("check")
        elif self.t3.get() == "" or self.t4.get() == "" or self.t5.get() == "" or self.t6.get() == "":
            messagebox.showwarning(None, "All fields are required for card addition")
        else:
            self.check_card("add")
            self.insert_card()

    def check_card(self, caller):
        query = f"SELECT * FROM card WHERE tier = '{self.t1.get()}' AND name = '{self.t2.get()}'"
        exist = check_table(query)

        if exist:
            messagebox.showwarning(None, "The card already exists.")
            self.clear_input()
        elif not exist and caller == "check":
            messagebox.showinfo(None, "The card does not exist.")

    def insert_card(self):
        gender = self.get_gender(self.v0.get())
        abil_1 = self.get_abil_1(self.v1.get())
        abil_2 = self.get_abil_2(self.v2.get())
        arrow = self.get_arrow(self.v3.get())

        query = f"INSERT INTO card VALUES (" \
                f"'{self.t1.get()}', " \
                f"\"{self.t2.get()}\", " \
                f"'{gender}', " \
                f"{self.t3.get()}, " \
                f"{self.t4.get()}, " \
                f"{self.t5.get()}, " \
                f"{self.t6.get()}, " \
                f"'{abil_1}', " \
                f"'{abil_2}', " \
                f"'{arrow}')"

        add_card(query)
        messagebox.showinfo(None, "New card created.")
        self.clear_input()

    def get_gender(self, i):
        switcher = {
            1: 'M',
            2: 'F'
        }

        return switcher.get(i)

    def get_abil_1(self, i):
        switcher = {
            1: 'POW',
            2: 'TGH',
            3: 'SPD',
            4: 'CHA'
        }

        return switcher.get(i)

    def get_abil_2(self, i):
        switcher = {
            1: 'POW',
            2: 'TGH',
            3: 'SPD',
            4: 'CHA'
        }

        return switcher.get(i)

    def get_arrow(self, i):
        switcher = {
            1: 'U',
            2: 'D',
            3: 'L',
            4: 'R'
        }

        return switcher.get(i)

    def clear_input(self):
        self.t3.delete(0, END)
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
