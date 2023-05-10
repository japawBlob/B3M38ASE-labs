import matplotlib.pyplot as plt
import numpy as np

def func ():
    pass

  
Vfan = [3, 4, 5, 6, 7, 8]
Airflow = []
Vbridge = [0.078, 0.124, 0.155, 0.177, 0.193, 0.204]
Ipt200 = [0.0462, 0.0507, 0.0531, 0.0557, 0.0570, 0.0586]
for i,j in zip(Vfan, Ipt200):
    air = int(round((0.000243 * i - 0.000481) * 1000000, 0))
    print ('|', air, '|', j, '|')
    Airflow.append(air)

plt.plot(Airflow, Vbridge)
plt.xlabel("$Airflow [cm^3/min]$")
plt.ylabel("$V_{bridge} [V]$")
plt.title("Open loop")
plt.show()  # show first chart
  
plt.figure()

# plt.plot(polyline, model1(polyline), "-.", color='green', label="fitted curve")
plt.plot(Airflow, Ipt200, label="measured data")
plt.xlabel("$Airflow [cm^3/min]$")
plt.ylabel("$I_{pt100} [A]$")
plt.legend()
plt.title("Closed loop")
plt.show()

flowSqrt = [np.sqrt(i) for i in Airflow]
Isquared = [i*i for i in Ipt200]

print(flowSqrt)
print(Isquared)

for i,j in zip(flowSqrt, Isquared):
    air = int(round((0.000243 * i - 0.000481) * 1000000, 0))
    print ('|', round(i,1), '|', round(j, 4), '|')
    # Airflow.append(air)

model1 = np.poly1d(np.polyfit(flowSqrt, Isquared, 1))
polyline = np.linspace(15, 40, 15)
print(model1)
plt.plot(flowSqrt, Isquared, label="measured data")
plt.plot(polyline, model1(polyline), "-.", color='green', label="fitted curve")
plt.xlabel("$\sqrt{Airflow} [\sqrt{cm^3/min}]$")
plt.ylabel("$(I_{pt100})^2 [A^2]$")
plt.legend()
plt.title("Characteristic")
plt.show()