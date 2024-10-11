import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def exponential_dist(avg):
    rate = 1/avg
    p = np.exp(-(rate*120))
    return p

p = exponential_dist(100)
print(p)
x = np.random.exponential(scale=0.50, size= 100)

plt.figure(figsize=(12,7))
np.random.seed(10)

sns.kdeplot(np.random.exponential(0.5, size=1000))
sns.kdeplot(np.random.exponential(1.0, size=1000))
sns.kdeplot(np.random.exponential(2.0, size=1000))
sns.kdeplot(np.random.exponential(4.0, size=1000))

plt.legend(['Rate: 0.5', 'Rate:1.0', 'Rate: 2.0', 'Rate: 4.0'])

plt.show()