import serial
from time import sleep, time
from matplotlib import pyplot as plt
from datetime import * 
print(time())

ser = serial.Serial('/dev/ttyACM0', 9600)

x = []
y = [[], []]


for i in range(500):
    line = ser.readline().decode('utf-8', errors='ignore').strip()
    data = line.split(",")
    
    x.append(int(data[0])/1000)
    y[0].append(int(data[1])/1024*5)
    y[1].append(int(data[2])/1024*5)  

print("DATA COLLECTED")
for y1 in y:
    plt.plot(x, y1)

print(x, y)
plt.minorticks_on()
plt.grid(True, which='both', axis='both')


plt.xlabel("czas [s]")
plt.ylabel("napiecie [V]")
plt.legend(["fotorezystor 1", "fotorezystor 2"])
plt.text(4, max(y[0]+y[1]), datetime.now())
poczatek = x[y[0].index(min(y[0]))]
koniec = x[y[1].index(min(y[1]))]

plt.title(f"Czas: {round(koniec-poczatek, 2)}s")
plt.show()
