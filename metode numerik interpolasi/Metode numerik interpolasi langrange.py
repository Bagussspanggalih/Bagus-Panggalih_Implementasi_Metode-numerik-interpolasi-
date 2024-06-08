import numpy as np
import matplotlib.pyplot as plt

# Data
tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])


def lagrange_interpolation(x, x_points, y_points):
    total = 0
    n = len(x_points)
    for i in range(n):
        xi = x_points[i]
        yi = y_points[i]
        
        def L(i, x):
            product = 1
            for j in range(n):
                if i != j:
                    xj = x_points[j]
                    product *= (x - xj) / (xi - xj)
            return product
        
        total += yi * L(i, x)
    return total


x_new = np.linspace(5, 40, 500)
y_new = [lagrange_interpolation(xi, tegangan, waktu_patah) for xi in x_new]


plt.figure(figsize=(10, 6))
plt.plot(tegangan, waktu_patah, 'o', label='Data Asli')
plt.plot(x_new, y_new, '-', label='Interpolasi Polinomial Lagrange')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinomial Lagrange')
plt.legend()
plt.grid(True)
plt.show()


for x in range(5, 45, 5):
    y = lagrange_interpolation(x, tegangan, waktu_patah)
    print(f'Tegangan: {x} kg/mm^2, Waktu Patah (interpolasi): {y:.2f} jam')
