import matplotlib.pyplot as plt


#Relativer Pfad der Textdatei für das Übertragen der Formel:
FormelPfad = "formel.txt"


#Lesen der Formel:
f = open(FormelPfad, "r")
FormelStr = f.read()
f.close
print(type(FormelStr))


#Der eingelesene String wird über das Aufrufen der Funktion für jeden X-Wert berechnet:
def str_to_func(FormelStr):
    return lambda x: eval(FormelStr)

#Legt das Intervall in einer Liste fest
domain = [x for x in range(-10,11)]

function = str_to_func(FormelStr)
#Liste in der die berechneten Werte gespeichert sind:
values = [function(x) for x in domain]
#Zeigt den Graphen mit Hilfe der Listen für das Intervall und die berechneten Werte
plt.plot(domain, values)
plt.show()