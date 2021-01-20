from tkinter import *
import tkinter.messagebox as mb


amount = 0.0
withdrawalcharges = 23
transactioncharge = 15


class transcWin():
    def __init__(self):
        self.pane = Tk()
        self.pane.title("welcome")
        self.pane.geometry("450x350")
        self.label = Label(self.pane, text="welcome", font="times 15 bold")
        self.label.place(x=85, y=5)
        self.lbl1 = Label(self.pane, text="balance", font="times  15 bold")
        self.lbl1.place(x=280, y=20)
        self.bal_display = Entry(self.pane, state="disabled")
        self.bal_display.place(x=280, y=40)
        self.label2 = Label(self.pane, text="username", font="times 15 bold")
        self.label2.place(x=5, y=25)
        self.ent2 = Entry(self.pane, state="disabled")
        self.ent2.place(x=5,y=45)
        self.label3 = Label(self.pane, text="do your transactions here", font="times 15 bold")
        self.label3.place(x=70, y=70)
        self.label4 = Label(self.pane, text="entr amnt", font="times 15 bold")
        self.label4.place(x=10, y=90)
        self.depo_ent= Entry(self.pane)
        self.depo_ent.place(x=10, y=120)
        self.depo_btn = Button(self.pane, text="Deposit", font="times 12 bold", command=self.deposit)
        self.depo_btn.place(x=10, y=150)
        self.label4 = Label(self.pane, text="enter amnt", font="times 15 bold")
        self.label4.place(x=280, y=90)
        self.withdraw_ent = Entry(self.pane)
        self.withdraw_ent.place(x=280, y=120)
        self.btn2 = Button(self.pane, text="Withdraw", font="times 12 bold")
        self.btn2.place(x=280, y=150)
        self.label5 = Label(self.pane, text="enter phone", font="times 15 bold")
        self.label5.place(x=10, y=200)
        self.phone_ent = Entry(self.pane)
        self.phone_ent.place(x=10, y=230)
        self.btn3 = Button(self.pane, text="send money", font="times 12 bold")
        self.btn3.place(x=10, y=260)


    def run(self):
        self.pane.mainloop()

    def deposit(self):
        depo = self.depo_ent.get()
        if depo == int:
          balance = amount + depo
          self.bal_display.get()
        else:
         mb.showinfo("error","Invalid number")








app = transcWin()
app.run()






