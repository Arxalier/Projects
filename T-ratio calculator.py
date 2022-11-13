import matplotlib.pyplot as plt
def sine(theta, accuracy):
    iterations = accuracy * 2
    sign = False
    x = 0
    f = 1
    for k in range(1, iterations + 2, 2):
        x = (((-1) ** int(sign)) * (theta ** k / f))+x
        sign = not sign
        f = ((k + 1) * (k + 2)) * f
    return x
angles = []
values = []
print(sine(30/57.296, 30))
pi = 3.1415926
for i in range(0, 7400, 20):
    angle = i/100
    while angle>=2*pi:
        angle-=2*pi
    angles.append(angle)
    values.append((sine(angle, 10)))
plt.plot(angles, values)
plt.waitforbuttonpress()
