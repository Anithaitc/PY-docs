from tkinter import *

adi = Tk()
adi.title("ANIL..(^_^)")
lab = Label(text="CALCULATOR", padx=100, fg="white", bg="#0261fa", ).grid(row=1, column=1, columnspan=5)

e = Entry(adi, font=('arial', 18, 'bold'), bg="#eee", width=21)

e.grid(row=2, column=0, columnspan=5)
t = ''


def btn_clear():
    e.delete(0, END)
    t = " "


def btn_click(n):
    global t
    if n == "c":
        e.delete(0, END)
        t = " "
    elif n == "e":
        e.delete(0, END)
        try:
            e.insert(0, eval(t))
        except:
            e.insert(0, "error")
    else:
        t = t + str(n)
        e.delete(0, END)
        e.insert(0, t)


b_1 = Button(adi, text="1", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(1)).grid(row=7, column=1)
b_2 = Button(adi, text="2", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(2)).grid(row=7, column=2)
b_3 = Button(adi, text="3", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(3)).grid(row=7, column=3)
b_4 = Button(adi, text="4", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(4)).grid(row=6, column=1)
b_5 = Button(adi, text="5", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(5)).grid(row=6, column=2)
b_6 = Button(adi, text="6", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(6)).grid(row=6, column=3)
b_7 = Button(adi, text="7", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(7)).grid(row=5, column=1)
b_8 = Button(adi, text="8", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(8)).grid(row=5, column=2)
b_9 = Button(adi, text="9", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(9)).grid(row=5, column=3)
b_0 = Button(adi, text="0", padx=25, pady=15, fg="black", bg="white", activebackground="grey", relief="ridge",
             command=lambda: btn_click(0)).grid(row=8, column=1)
b_clear = Button(adi, text="C", padx=25, pady=15, fg="white", bg="#072657", activebackground="grey", relief="ridge",
                 command=lambda: btn_click('c')).grid(row=4, column=1)
b_div = Button(adi, text="/", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click("/")).grid(row=4, column=2)
b_mul = Button(adi, text="X", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click('*')).grid(row=4, column=3)
b_rp = Button(adi, text="(", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
              command=lambda: btn_click('(')).grid(row=4, column=4)
b_lp = Button(adi, text=")", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
              command=lambda: btn_click(')')).grid(row=5, column=4)
b_sub = Button(adi, text="-", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click("-")).grid(row=6, column=4)
b_add = Button(adi, text="+", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click("+")).grid(row=7, column=4)
b_eq = Button(adi, text="=", padx=25, pady=15, fg="white", bg="#03ad09", activebackground="#0c590f", relief="ridge",
              command=lambda: btn_click('e')).grid(row=8, column=4)
b_pow = Button(adi, text="^", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click("**")).grid(row=8, column=3)
b_dec = Button(adi, text=".", padx=25, pady=15, fg="white", bg="#737475", activebackground="grey", relief="ridge",
               command=lambda: btn_click(".")).grid(row=8, column=2)

adi.mainloop()