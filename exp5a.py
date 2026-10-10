import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Line
plt.plot(x, y, linewidth=2)

# Highlight points
plt.scatter(x, y, color='red', s=100, edgecolors='black', zorder=5)

# Point values
for i in range(len(x)):
    plt.annotate(
        f'({x[i]}, {y[i]})',
        (x[i], y[i]),
        xytext=(0, 10),
        textcoords='offset points',
        ha='center',
        fontweight='bold'
    )

plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)

plt.show()