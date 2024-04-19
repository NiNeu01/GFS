import matplotlib.pyplot as plt
import numpy as np

array1= 0
array2= 4
array3= 1
dataWord= float

# evenly sampled time at 200ms intervals
x = np.linspace(array1, array2, array3, dataWord)
t = open("test.txt", "r")
print(t.readline())
formel = t.readline()


fig, ax = plt.subplots()

plt.plot(x, formel)

ax.set(xlim=(array1, array2), xticks=np.linspace(array1, array2, array3, dataWord),
       ylim=(array1*10, array2*10), yticks=np.linspace(array1*10, array2*10, 1))

plt.show()

