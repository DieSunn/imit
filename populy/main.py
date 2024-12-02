import numpy as np
import matplotlib.pyplot as plt

# Начальные параметры
A_init = 1000  # Начальная численность армии A
B_init = 1200  # Начальная численность армии B
alpha = 0.1    # Эффективность армии A
beta = 0.08    # Эффективность армии B
r_A = 5        # Скорость пополнения армии A
r_B = 3        # Скорость пополнения армии B
max_A = 1500   # Максимальный размер армии A
max_B = 1500   # Максимальный размер армии B
t_max = 100    # Общее время моделирования
dt = 0.1       # Шаг времени

# Функция для моделирования
def simulate_war(A_init, B_init, alpha, beta, r_A, r_B, max_A, max_B, t_max, dt):
    t = np.arange(0, t_max, dt)
    A = np.zeros_like(t)
    B = np.zeros_like(t)
    A[0] = A_init
    B[0] = B_init

    for i in range(1, len(t)):
        dA = -beta * B[i-1] + r_A
        dB = -alpha * A[i-1] + r_B

        # Обновление численности с учётом максимума
        A[i] = min(A[i-1] + dA * dt, max_A)
        B[i] = min(B[i-1] + dB * dt, max_B)

        # Если одна из армий уничтожена, бой заканчивается
        if A[i] <= 0 or B[i] <= 0:
            A[i:] = max(A[i], 0)
            B[i:] = max(B[i], 0)
            break

    return t, A, B

# Запуск симуляции
t, A, B = simulate_war(A_init, B_init, alpha, beta, r_A, r_B, max_A, max_B, t_max, dt)

# График численности армий
plt.figure(figsize=(10, 6))
plt.plot(t, A, label='Army A', color='blue')
plt.plot(t, B, label='Army B', color='red')
plt.xlabel('Time')
plt.ylabel('Army Size')
plt.legend()
plt.title('War Model')
plt.grid()
plt.show()