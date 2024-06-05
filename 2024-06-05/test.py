import tkinter as tk
import subprocess

window = tk.Tk()
window.title("f(x)=")

# Hier kann man die Dateipfade des Scripts zum Anzeigen des Graphen und der Textdatei zur Übergabe der Funktion definieren:
PlotterScript = "interpreter-test2.py"
FormelPfad = "demo.txt"

# Hier sind Anpassungen des Aussehens der Buttons möglich
ButtonBreite = 5
ButtonBreite2 = 15
ButtonHoehe = 5

ButtonFont = ('Times 15')
AnzeigeFont = ('Times 20')

ButtonFarbeZahl = "Lawn Green"
ButtonFarbeOperatoren = "khaki"
ButtonFarbeKlammern = "SteelBlue1"
ButtonFarbeAktionen = "firebrick2"

AnzeigeFeldBreite = ButtonBreite * 3






# Hier wird das Textfeld zur Anzeige der eingegebenen Funktion erstellt
display_text = tk.StringVar()
display = tk.Label(window, textvariable=display_text, bg="SteelBlue4", font=AnzeigeFont, width=AnzeigeFeldBreite)
display.grid(row=0, columnspan=7)

# Hier wird die Datei zur Übergabe der Formel geleert, um Fehler zu vermeiden:
f = open(FormelPfad, "w")
f.write("")
f.close()

# Hier werden die Funktionen, die von den Buttons aufgerufen werden, definiert:

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

# Hier werden die Buttons erstellt, die in einer unsichtbaren Tabelle im Fenster positioniert werden.

buttong = tk.Button(window, text="1",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl1)
buttong.grid(row=1, column=0)

buttong = tk.Button(window, text="2",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl2)
buttong.grid(row=1, column=1)

buttong = tk.Button(window, text="3",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl3)
buttong.grid(row=1, column=2)

buttong = tk.Button(window, text="4",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl4)
buttong.grid(row=2, column=0)

buttong = tk.Button(window, text="5",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl5)
buttong.grid(row=2, column=1)

buttong = tk.Button(window, text="6",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl6)
buttong.grid(row=2, column=2)

buttong = tk.Button(window, text="7",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl7)
buttong.grid(row=3, column=0)

buttong = tk.Button(window, text="8",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl8)
buttong.grid(row=3, column=1)

buttong = tk.Button(window, text="9",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl9)
buttong.grid(row=3, column=2)

buttong = tk.Button(window, text="0",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command=zahl0)
buttong.grid(row=4, column=1)


platzhalter = tk.Label(window, text="",  width=ButtonBreite)
platzhalter.grid(row=1, column=4)


buttong = tk.Button(window, text="+",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command=plus)
buttong.grid(row=1, column=5)

buttong = tk.Button(window, text="-",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command=minus)
buttong.grid(row=2, column=5)

buttong = tk.Button(window, text="*",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command=mal)
buttong.grid(row=3, column=5)

buttong = tk.Button(window, text=":",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command=geteilt)
buttong.grid(row=4, column=5)


buttong = tk.Button(window, text="(",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command=klammerAuf)
buttong.grid(row=1, column=6)

buttong = tk.Button(window, text=")",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command=klammerZu)
buttong.grid(row=2, column=6)

buttong = tk.Button(window, text="X",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command=x)
buttong.grid(row=1, column=7)

buttong = tk.Button(window, text="Potenz",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command=potenz)
buttong.grid(row=3, column=6)


buttong = tk.Button(window, text="In Graph umwandeln",  width=ButtonBreite2, font=ButtonFont, bg=ButtonFarbeAktionen, command=lambda:[umwandeln(),DateiLeeren()])
buttong.grid(row=4, column=7)

buttong = tk.Button(window, text="Formel löschen",  width=ButtonBreite2, font=ButtonFont, bg=ButtonFarbeAktionen, command=DateiLeeren)
buttong.grid(row=3, column=7)




window.mainloop()