import tkinter as tk
import subprocess

window = tk.Tk()
window.title("f(x)=")

# Hier kann man die Dateipfade des Scripts zum Anzeigen des Graphen und der Textdatei zur Übergabe der Funktion definieren:
PlotterScript = "interpreter.py"
FormelPfad = "formel.txt"

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

# Hier wird die Funktionen, die von den Buttons aufgerufen werden, definiert:

def zahl(NummerInt):
    NummerStr = str(NummerInt)
    if NummerStr == "^":
        f = open(FormelPfad, "a")
        f.write("**")
        f.close()
        s = display_text.get()
        s += "^"
        display_text.set(s)

    elif NummerStr == "clear":
        f = open(FormelPfad, "w")
        f.write("")
        f.close()
        s = ''
        display_text.set(s)

    elif NummerStr == "calc":
        subprocess.run(["python", PlotterScript])
        s = 'In Graph umgewandelt'
        display_text.set(s)

    else:
        f = open(FormelPfad, "a")
        f.write(NummerStr)
        f.close()
        s = display_text.get()
        s += NummerStr
        display_text.set(s)

effonix = tk.Label(window, text="f(x)=", bg="SteelBlue4", font=AnzeigeFont,)
effonix.grid(row=0, column=0)

# Hier werden die Buttons erstellt, die in einem Raster im Fenster positioniert werden.

buttong = tk.Button(window, text="1",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(1))
buttong.grid(row=1, column=0)

buttong = tk.Button(window, text="2",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(2))
buttong.grid(row=1, column=1)

buttong = tk.Button(window, text="3",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(3))
buttong.grid(row=1, column=2)

buttong = tk.Button(window, text="4",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(4))
buttong.grid(row=2, column=0)

buttong = tk.Button(window, text="5",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(5))
buttong.grid(row=2, column=1)

buttong = tk.Button(window, text="6",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(6))
buttong.grid(row=2, column=2)

buttong = tk.Button(window, text="7",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(7))
buttong.grid(row=3, column=0)

buttong = tk.Button(window, text="8",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(8))
buttong.grid(row=3, column=1)

buttong = tk.Button(window, text="9",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(9))
buttong.grid(row=3, column=2)

buttong = tk.Button(window, text="0",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeZahl, command= lambda: zahl(0))
buttong.grid(row=4, column=1)


platzhalter = tk.Label(window, text="",  width=ButtonBreite)
platzhalter.grid(row=1, column=4)


buttong = tk.Button(window, text="+",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command= lambda: zahl("+"))
buttong.grid(row=1, column=5)

buttong = tk.Button(window, text="-",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command= lambda: zahl("-"))
buttong.grid(row=2, column=5)

buttong = tk.Button(window, text="*",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command= lambda: zahl("*"))
buttong.grid(row=3, column=5)

buttong = tk.Button(window, text=":",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeOperatoren, command= lambda: zahl(":"))
buttong.grid(row=4, column=5)


buttong = tk.Button(window, text="(",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command= lambda: zahl("("))
buttong.grid(row=1, column=6)

buttong = tk.Button(window, text=")",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command= lambda: zahl(")"))
buttong.grid(row=2, column=6)

buttong = tk.Button(window, text="X",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command= lambda: zahl("x"))
buttong.grid(row=1, column=7)

buttong = tk.Button(window, text="Potenz",  width=ButtonBreite, font=ButtonFont, bg=ButtonFarbeKlammern, command= lambda: zahl("^"))
buttong.grid(row=3, column=6)


buttong = tk.Button(window, text="In Graph umwandeln",  width=ButtonBreite2, font=ButtonFont, bg=ButtonFarbeAktionen, command=lambda:[zahl("calc"),zahl("clear")])
buttong.grid(row=4, column=7)

buttong = tk.Button(window, text="Formel löschen",  width=ButtonBreite2, font=ButtonFont, bg=ButtonFarbeAktionen, command= lambda: zahl("clear"))
buttong.grid(row=3, column=7)




window.mainloop()