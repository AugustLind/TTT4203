import numpy as np
import matplotlib.pyplot as plt

# Data
i = np.array([90, 46.05, 23.28, 9.35])
v = np.array([9, 9.21, 9.31, 9.35])

# Utfør lineær regresjon
coefficients = np.polyfit(i, v, 1)
a, b = coefficients

# Lag en regresjonslinje
regression_line = a * i + b

# Plot datapunktene og regresjonslinjen
plt.scatter(i, v, label='Data')
plt.plot(i, regression_line, color='red', label='Regresjonslinje')
plt.xlabel('i-verdier')
plt.ylabel('v-verdier')
plt.legend()
plt.grid(True)
plt.plot(i,v)

# Vis plottet
plt.show()

# Skriv ut regresjonskoeffisientene
print(f"Regresjonskoeffisienter: Slope = {a}, Intercept = {b}")
