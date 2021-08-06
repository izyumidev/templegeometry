import matplotlib.pyplot as plt
import math

n = 3  # number of layers
R = 1  # radius of big circle
X = 0  # x coordinate of the center of the big circle
Y = 0  # y coordinate of the center of the big circle

n -= 1
figure, axes = plt.subplots()
axes.add_artist(plt.Circle((X, Y), R, fill=False))
r = math.sqrt(3) / (2 * n + math.sqrt(3))
A = [X, R - r]
axes.add_artist(plt.Circle((A[0], A[1]), r, fill=False))
for i in range(n + 1):
    if i != 0:
        y = A[1] - i * math.sqrt(3) * r
        left = A[0] - i * r
        axes.add_artist(plt.Circle((left, y), r, fill=False))
        for j in range(i):
            axes.add_artist(plt.Circle((left + (j + 1) * 2 * r, y), r, fill=False))
axes.set_xlim([X - R, X + R])
axes.set_ylim([Y - R, Y + R])
axes.set_aspect(1)
plt.show()
