import matplotlib.pyplot as plt
import numpy as np

FormelPfad = "tkinter-büttongs\demo.txt"

f = open(FormelPfad, "r")
#print(f.read())
FormelStr = f.read()
f.close
print(FormelStr)

Formel = eval(FormelStr)

print(Formel)

# Data for plotting
x = np.arange(-10.0, 10.0, 0.01)
s = Formel

fig, ax = plt.subplots()
ax.plot(x, s)

ax.set(xlabel='X', ylabel='Y',
       title='Funktion:')
ax.grid()

fig.savefig("test.png")
plt.show()