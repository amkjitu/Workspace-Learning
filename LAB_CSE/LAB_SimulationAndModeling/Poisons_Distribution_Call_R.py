from scipy.stats import poisson
import matplotlib.pyplot as plt
#
# Random variable representing number of restaurants
# Mean number of occurences of restaurants in 10 KM is 2
#
X = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
lmbda = 5
#
# Probability values
#
poisson_pd = poisson.pmf(X, lmbda)
#
# Plot the probability distribution
#
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, poisson_pd, 'bo', ms=8, label='poisson pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. Receiving Call", fontsize="18")
plt.title("Poisson Distribution - No. of Receiving call Vs Probability", fontsize="18")
ax.vlines(X, 0, poisson_pd, colors='b', lw=5, alpha=0.5)
plt.show()

from scipy.stats import poisson
import matplotlib.pyplot as plt
#
# Random variable representing number of restaurants
# Mean number of occurences of restaurants in 10 KM is 2
#
X = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
lmbda = 10
#
# Probability values
#
poisson_pd = poisson.pmf(X, lmbda)
#
# Plot the probability distribution
#
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, poisson_pd, 'bo', ms=8, label='poisson pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. Receiving Call", fontsize="18")
plt.title("Poisson Distribution - No. of Receiving call Vs Probability", fontsize="18")
ax.vlines(X, 0, poisson_pd, colors='b', lw=5, alpha=0.5)
plt.show()

from scipy.stats import poisson
import matplotlib.pyplot as plt
#
# Random variable representing number of restaurants
# Mean number of occurences of restaurants in 10 KM is 2
#
X = [0, 1, 2, 3, 4, 5,6,7,8,9,10]
lmbda = 15
#
# Probability values
#
poisson_pd = poisson.pmf(X, lmbda)
#
# Plot the probability distribution
#
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.plot(X, poisson_pd, 'bo', ms=8, label='poisson pmf')
plt.ylabel("Probability", fontsize="18")
plt.xlabel("X - No. Receiving Call", fontsize="18")
plt.title("Poisson Distribution - No. of Receiving call Vs Probability", fontsize="18")
ax.vlines(X, 0, poisson_pd, colors='b', lw=5, alpha=0.5)
plt.show()