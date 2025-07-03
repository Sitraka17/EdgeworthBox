!pip install matplotlib numpy ipywidgets

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# Utility functions for both agents
def uA(x, y, alpha=0.5):
    return (x**alpha) * (y**(1 - alpha))

def uB(x, y, beta=0.5):
    return (x**beta) * (y**(1 - beta))

# Indifference curve for Agent A
def indifference_curve_A(u, alpha, x_vals):
    return (u / (x_vals**alpha))**(1 / (1 - alpha))

# Indifference curve for Agent B in the Edgeworth box (flipped axes)
def indifference_curve_B(u, beta, x_vals, total_x, total_y):
    xB = x_vals
    yB = (u / (xB**beta))**(1 / (1 - beta))
    return total_y - yB, total_x - xB

def plot_edgeworth_box(xA_endow, yA_endow, alpha, beta, uA_level, uB_level):
    # Total resources in the economy
    total_x = 10
    total_y = 10

    # Setup the plot
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_xlim(0, total_x)
    ax.set_ylim(0, total_y)
    ax.set_xlabel('Good X (A left, B right)')
    ax.set_ylabel('Good Y (A bottom, B top)')
    ax.set_title('Edgeworth Box')

    # Plot initial endowment
    ax.plot(xA_endow, yA_endow, 'ro', label='Initial Endowment')

    # Plot Agent A's indifference curve
    x_vals = np.linspace(0.1, total_x - 0.1, 100)
    y_vals_A = indifference_curve_A(uA_level, alpha, x_vals)
    ax.plot(x_vals, y_vals_A, 'b-', label="A's indifference curve")

    # Plot Agent B's indifference curve
    y_vals_B, x_vals_B = indifference_curve_B(uB_level, beta, x_vals, total_x, total_y)
    ax.plot(x_vals_B, y_vals_B, 'g--', label="B's indifference curve")

    # Box boundaries
    ax.plot([0, total_x, total_x, 0, 0], [0, 0, total_y, total_y, 0], 'k--')

    # Twin axes for B
    ax2 = ax.twinx().twiny()
    ax2.set_xlim(total_x, 0)
    ax2.set_ylim(total_y, 0)
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_xlabel("Good X for B")
    ax2.set_ylabel("Good Y for B")

    ax.legend()
    plt.grid(True)
    plt.show()

# Interactive widget
interact(
    plot_edgeworth_box,
    xA_endow=FloatSlider(min=1, max=9, step=0.5, value=5, description="xA endow"),
    yA_endow=FloatSlider(min=1, max=9, step=0.5, value=5, description="yA endow"),
    alpha=FloatSlider(min=0.1, max=0.9, step=0.1, value=0.5, description="Alpha A"),
    beta=FloatSlider(min=0.1, max=0.9, step=0.1, value=0.5, description="Beta B"),
    uA_level=FloatSlider(min=1, max=25, step=1, value=10, description="Utility A"),
    uB_level=FloatSlider(min=1, max=25, step=1, value=10, description="Utility B"),
)

