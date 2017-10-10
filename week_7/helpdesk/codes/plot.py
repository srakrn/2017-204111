import math
import matplotlib.pyplot as plt
import numpy as np
from fibonacci_recursion import measure_time, fibonacci

config = {
    "regression": "exponential"
}

start, stop = list(map(int, input("Enter init and final value: ").split()))
n = np.arange(start, stop, 1)
t = []
for v in n:
    time, fib = measure_time(fibonacci, v)
    t.append(time)
t = np.array(t)

if config["regression"] == "linear":
    polyfit = np.polyfit(n, t, 1)
elif config["regression"] == "exponential":
    polyfit = np.polyfit(n, np.log(t), 1)

r = []
for v in n:
    if config["regression"] == "linear":
        r.append(polyfit[0]*v + polyfit[1]) 
    elif config["regression"] == "exponential":
        r.append(math.e**polyfit[1] * math.e**(polyfit[0]*v))
r = np.array(r)

# We create plots and subplots.
# Graphs should be plotted into ax
fig, ax = plt.subplots()

ax.set(xlabel='n', ylabel='time (s)', title='Time measurement for function call')
ax.grid()

if config["regression"] == "linear":
    eq = "y={:.3f}x+{:.3f}".format(polyfit[0], polyfit[1])
elif config["regression"] == "exponential":
    eq = "y={:.3f}e^{:.3f}x".format(math.e**polyfit[0], polyfit[1])

ax.plot(n, t, label="time plot")
ax.plot(n, r, label=eq)

plt.legend()

fig.savefig("test.png")
plt.show()

guess = int(input())
print(math.e**polyfit[1] * math.e**(polyfit[0]*guess))
