import matplotlib.pyplot as plt

FormelPfad = "tkinter-büttongs\demo.txt"



f = open(FormelPfad, "r")
#print(f.read())
FormelStr = f.read()
f.close
print(type(FormelStr))

def str_to_func(FormelStr):
    return lambda x: eval(FormelStr)

domain = [x for x in range(-10,10)]
range = [x ** 2 + x * 2 + 1 for x in domain]

function = str_to_func(FormelStr)
values = [function(x) for x in domain]
plt.plot(domain, values)
plt.show()