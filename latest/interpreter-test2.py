import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

FormelPfad = "demo.txt"

#IAnfang = 1
#IEnde = -2

window = tk.Tk()

tk.Label(window, text="Intervall Anfang").grid(row=0)
tk.Label(window, text="Intervall Ende (Eingabe ohne Minus davor!)").grid(row=1)

Eingabe1 = tk.Entry(window)
Eingabe2 = tk.Entry(window)


Eingabe1.grid(row=0, column=1)
Eingabe2.grid(row=1, column=1)




#A = int(IAnfang)
#E = int(IEnde)


#print(A)




def ZeigeGraph():
    IAnfang = Eingabe1.get()
    IEnde = Eingabe2.get()
    print(IAnfang)
    IAnfangInt = int(IAnfang)
    type(IAnfangInt)

    f = open(FormelPfad, "r")
    #print(f.read())
    FormelStr = f.read()
    f.close
    print(type(FormelStr))

    def str_to_func(FormelStr):
        return lambda x: eval(FormelStr)

    #domain = [x for x in range(-5,5)]
    #range = [x ** 2 + x * 2 for x in domain]

   
#"-" + IEnde
    

    domain = np.arange(5,5 , 0.01)


    function = str_to_func(FormelStr)
    values = [function(x) for x in domain]
    plt.plot(domain, values)
    plt.show()

buttong = tk.Button(window, text="Zeige den graph!", height=2, width=15, command=ZeigeGraph)
buttong.grid(row=2, column=1)

window.mainloop()