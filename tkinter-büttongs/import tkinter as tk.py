import tkinter as tk



#Grundrechenarten:
def addition():
    f = open("demo.txt", "a")
    f.write("+")
    f.close()
    label3 = tk.Label(root, text="+")
    label3.pack()

def subtraktion():
    f = open("demo.txt", "a")
    f.write("-")
    f.close()
    label3 = tk.Label(root, text="-")
    label3.pack()

def multiplikation():
    f = open("demo.txt", "a")
    f.write("*")
    f.close()
    label3 = tk.Label(root, text="*")
    label3.pack()

def division():
    f = open("demo.txt", "a")
    f.write(":")
    f.close()
    label3 = tk.Label(root, text=":")
    label3.pack()


#Klammern
def klammerAuf():
    f = open("demo.txt", "a")
    f.write("(")
    f.close()
    label3 = tk.Label(root, text="(")
    label3.pack()

def klammerZu():
    f = open("demo.txt", "a")
    f.write(")")
    f.close()
    label3 = tk.Label(root, text=")")
    label3.pack()


#Zahleneingabe:
def Zahleneingabe():
    # print(eingabefeld_wert.get())
    zahl = float(eingabefeld_wert.get())
    
    textausgabe.pack()


root = tk.Tk()
eingabefeld_wert=tk.StringVar()
eingabefeld=tk.Entry(root, textvariable=eingabefeld_wert)
eingabefeld.pack()


#Grundrechenarten:

schaltf1 = tk.Button(root, text="addition", command=addition)
schaltf1.pack()

schaltf2 = tk.Button(root, text="subtraktion", command=subtraktion)
schaltf2.pack()

schaltf3 = tk.Button(root, text="multiplikation", command=multiplikation)
schaltf3.pack()

schaltf4 = tk.Button(root, text="division", command=division)
schaltf4.pack()

#Zahleneingabe:
schaltf1 = tk.Button(root, text="Aktion durchführen", command=Zahleneingabe)
schaltf1.pack()

#Klammern:
schaltf5 = tk.Button(root, text="(", command=klammerAuf)
schaltf5.pack()

schaltf6 = tk.Button(root, text=")", command=klammerZu)
schaltf6.pack()

root.mainloop()