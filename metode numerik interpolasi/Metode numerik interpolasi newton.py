import numpy as np
import matplotlib.pyplot as plt

# Data
tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])


def divided_differences(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    return coef[0, :]


def newton_interpolation(x, x_points, coef):
    n = len(coef)
    total = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_points[j])
        total += term
    return total


coef = divided_differences(tegangan, waktu_patah)


x_new = np.linspace(5, 40, 500)
y_new = [newton_interpolation(xi, tegangan, coef) for xi in x_new]


plt.figure(figsize=(10, 6))
plt.plot(tegangan, waktu_patah, 'o', label='Data Asli')
plt.plot(x_new, y_new, '-', label='Interpolasi Polinomial Newton')
plt.xlabel('Tegangan (kg/mm^2)')
plt.ylabel('Waktu Patah (jam)')
plt.title('Interpolasi Polinomial Newton')
plt.legend()
plt.grid(True)
plt.show()


for x in range(5, 45, 5):
    y = newton_interpolation(x, tegangan, coef)
    print(f'Tegangan: {x} kg/mm^2, Waktu Patah (interpolasi): {y:.2f} jam')
