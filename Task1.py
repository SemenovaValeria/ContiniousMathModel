import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols('t')

x_t = (32/3)*sp.exp(-5*t) - (2/3)*sp.exp(2*t) + 2
y_t = (32/3)*sp.exp(-5*t) + (4/3)*sp.exp(2*t) + 3

x_initial = x_t.subs(t, 0)
y_initial = y_t.subs(t, 0)

print(f"x(0) = 12 is met: {x_initial == 12}")
print(f"y(0) = 15 is met: {y_initial == 15}")

def x_t_general(t, C, D):
    return C * np.exp(-5*t) + D*np.exp(2*t) + 2

def y_t_general(t, C, D):
    return -2*C * np.exp(-5*t) + D*np.exp(2*t) + 3

initial_conditions = [
    (12, 15),
    (10, 10),
    (5, 20),
    (20, 5)
]

t_values = np.linspace(0, 1, 500)

plt.figure(figsize=(14, 7))

for A_value, B_value in initial_conditions:
    C_value = (A_value - B_value + 1) / 3
    D_value = (2*A_value + B_value - 7) / 3

    x_values = x_t_general(t_values, C_value, D_value)
    y_values = y_t_general(t_values, C_value, D_value)

    plt.plot(t_values, x_values, label=f'x(t) with A={A_value}, B={B_value}')
    plt.plot(t_values, y_values, label=f'y(t) with A={A_value}, B={B_value}', linestyle='--')

plt.title('Long-term behavior with various initial conditions')
plt.xlabel('Time')
plt.ylabel('Values of x(t) and y(t)')
plt.legend()
plt.grid(True)
plt.show()