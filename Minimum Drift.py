# River is 100m wide, and flows at 10 m/s. Swimmer can swim at max speed of 5 m/s. What is the minimum attainable drift?
import math
import matplotlib.pyplot as plt
thetas = []
drifts = []
for i in range(1, 91):
    theta = i/57.2
    thetas.append(i)
    xComponent = 100*math.cos(theta)
    yComponent = 50*math.sin(theta)
    # 100 = UyT, T = 100/Uy
    t = 100/yComponent
    drift = (xComponent-10)*t
    drifts.append(abs(drift))
plt.plot(thetas, drifts)
plt.show() # v = s/t, s = vt