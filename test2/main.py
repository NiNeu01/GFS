import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

formel = int(input("Formel eingeben (Ohne y= oder f(x)= ; Potenzen: x hoch 2 -> x**2): "))
print("Formel ist: " + formel)

os.system("Datei-schreiben.py 1")

f = open("formel.txt", "a")
f.write(formel)
f.close


# make data
x = np.linspace(0, 10, 100)
y = x

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(-4, 4), xticks=np.arange(-4, 4),
       ylim=(-4, 4), yticks=np.arange(-4, 4))

plt.show()
