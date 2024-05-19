import tkinter as tk

root = tk.Tk()
root.title("Formeleingabe")
display_text = tk.StringVar()
display = tk.Label(root, textvariable=display_text)
display.pack
#vorschau = tk.Label(root, textvariable=display_text).pack()

#Grundrechenarten:
def addition():
    f = open("demo.txt", "a")
    f.write("+")
    f.close()
    s = display_text.get()
    s += str("+")
    display_text.set(s)

schaltf1 = tk.Button(root, text="addition", command=addition)
schaltf1.pack()