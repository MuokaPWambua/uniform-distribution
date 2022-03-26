import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

values =  np.random.uniform(-10.0, 10.0, 100000)

plt.title("Uniform Distribution")
plt.hist(values, 50)

plt.show()
