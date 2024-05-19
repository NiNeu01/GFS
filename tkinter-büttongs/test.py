import tkinter as tk
import subprocess

window = tk.Tk()

# Creating main label
display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text)
display.grid(row=0, columnspan=7)

PlotterScript = "tkinter-büttongs\interpreter-test2.py"
FormelPfad = "tkinter-büttongs\demo.txt"

f = open(FormelPfad, "w")
f.write("")
f.close()



def zahl0():
    f = open(FormelPfad, "a")
    f.write("0")
    f.close()
    s = display_text.get()
    s += '0'
    display_text.set(s)

def zahl1():
    f = open(FormelPfad, "a")
    f.write("1")
    f.close()
    s = display_text.get()
    s += '1'
    display_text.set(s)

def zahl2():
    f = open(FormelPfad, "a")
    f.write("2")
    f.close()
    s = display_text.get()
    s += '2'
    display_text.set(s)

def zahl3():
    f = open(FormelPfad, "a")
    f.write("3")
    f.close()
    s = display_text.get()
    s += '3'
    display_text.set(s)

def zahl4():
    f = open(FormelPfad, "a")
    f.write("4")
    f.close()
    s = display_text.get()
    s += '4'
    display_text.set(s)

def zahl5():
    f = open(FormelPfad, "a")
    f.write("5")
    f.close()
    s = display_text.get()
    s += '5'
    display_text.set(s)

def zahl6():
    f = open(FormelPfad, "a")
    f.write("6")
    f.close()
    s = display_text.get()
    s += '6'
    display_text.set(s)

def zahl7():
    f = open(FormelPfad, "a")
    f.write("7")
    f.close()
    s = display_text.get()
    s += '7'
    display_text.set(s)

def zahl8():
    f = open(FormelPfad, "a")
    f.write("8")
    f.close()
    s = display_text.get()
    s += '8'
    display_text.set(s)

def zahl9():
    f = open(FormelPfad, "a")
    f.write("9")
    f.close()
    s = display_text.get()
    s += '9'
    display_text.set(s)





def plus():
    f = open(FormelPfad, "a")
    f.write("+")
    f.close()
    s = display_text.get()
    s += '+'
    display_text.set(s)

def minus():
    f = open(FormelPfad, "a")
    f.write("-")
    f.close()
    s = display_text.get()
    s += '-'
    display_text.set(s)

def mal():
    f = open(FormelPfad, "a")
    f.write("*")
    f.close()
    s = display_text.get()
    s += '*'
    display_text.set(s)

def geteilt():
    f = open(FormelPfad, "a")
    f.write(":")
    f.close()
    s = display_text.get()
    s += ':'
    display_text.set(s)



def x():
    f = open(FormelPfad, "a")
    f.write("x")
    f.close()
    s = display_text.get()
    s += 'x'
    display_text.set(s)

def potenz():
    f = open(FormelPfad, "a")
    f.write("**")
    f.close()
    s = display_text.get()
    s += '^'
    display_text.set(s)



def klammerAuf():
    f = open(FormelPfad, "a")
    f.write("(")
    f.close()
    s = display_text.get()
    s += '('
    display_text.set(s)

def klammerZu():
    f = open(FormelPfad, "a")
    f.write(")")
    f.close()
    s = display_text.get()
    s += ')'
    display_text.set(s)

def umwandeln():
    subprocess.run(["python", PlotterScript])
    
    s = 'In Graph umgewandelt'
    display_text.set(s)

def DateiLeeren():
    f = open(FormelPfad, "w")
    f.write("")
    f.close()
    s = ''
    display_text.set(s)


buttong = tk.Button(window, text="1", height=5, width=5, command=zahl1)
buttong.grid(row=1, column=0)

buttong = tk.Button(window, text="2", height=5, width=5, command=zahl2)
buttong.grid(row=1, column=1)

buttong = tk.Button(window, text="3", height=5, width=5, command=zahl3)
buttong.grid(row=1, column=2)

buttong = tk.Button(window, text="4", height=5, width=5, command=zahl4)
buttong.grid(row=2, column=0)

buttong = tk.Button(window, text="5", height=5, width=5, command=zahl5)
buttong.grid(row=2, column=1)

buttong = tk.Button(window, text="6", height=5, width=5, command=zahl6)
buttong.grid(row=2, column=2)

buttong = tk.Button(window, text="7", height=5, width=5, command=zahl7)
buttong.grid(row=3, column=0)

buttong = tk.Button(window, text="8", height=5, width=5, command=zahl8)
buttong.grid(row=3, column=1)

buttong = tk.Button(window, text="9", height=5, width=5, command=zahl9)
buttong.grid(row=3, column=2)

buttong = tk.Button(window, text="0", height=5, width=5, command=zahl0)
buttong.grid(row=4, column=1)


platzhalter = tk.Label(window, text="", height=5, width=5)
platzhalter.grid(row=1, column=4)


buttong = tk.Button(window, text="+", height=5, width=5, command=plus)
buttong.grid(row=1, column=5)

buttong = tk.Button(window, text="-", height=5, width=5, command=minus)
buttong.grid(row=2, column=5)

buttong = tk.Button(window, text="*", height=5, width=5, command=mal)
buttong.grid(row=3, column=5)

buttong = tk.Button(window, text=":", height=5, width=5, command=geteilt)
buttong.grid(row=4, column=5)


buttong = tk.Button(window, text="(", height=5, width=5, command=klammerAuf)
buttong.grid(row=1, column=6)

buttong = tk.Button(window, text=")", height=5, width=5, command=klammerZu)
buttong.grid(row=2, column=6)

buttong = tk.Button(window, text="X", height=5, width=5, command=x)
buttong.grid(row=1, column=7)

buttong = tk.Button(window, text="Potenz", height=5, width=5, command=potenz)
buttong.grid(row=3, column=6)


buttong = tk.Button(window, text="In Graph umwandeln", height=5, width=15, command=lambda:[umwandeln(),DateiLeeren()])
buttong.grid(row=4, column=7)

buttong = tk.Button(window, text="Formel löschen", height=5, width=15, command=DateiLeeren)
buttong.grid(row=3, column=7)




window.mainloop()