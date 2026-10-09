import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Uniform(a,b)
a = 20
b = 40
rv = stats.uniform(loc=a, scale=b-a)

# x values for the PDF and CDF
x = np.linspace(a-5, b+5, 500)

# Use the formulas derived above
pdf = np.where((x >= a) & (x <= b), 1/(b-a), 0)
cdf = np.where(
    x < a,
    0,
    np.where(x <= b, (x-a)/(b-a), 1)
)

# p values for the quantile function
p = np.linspace(0, 1, 500)
quantile = a + p*(b-a)

# Plot all three functions
fig, ax = plt.subplots(1, 3, figsize=(13, 4))

ax[0].plot(x, pdf)
ax[0].set_xlabel("x")
ax[0].set_ylabel("f_X(x)")
ax[0].set_title("PDF")
ax[0].grid(alpha=0.25)

ax[1].plot(x, cdf)
ax[1].set_xlabel("x")
ax[1].set_ylabel("F_X(x)")
ax[1].set_title("CDF")
ax[1].set_ylim(-0.05, 1.05)
ax[1].grid(alpha=0.25)

ax[2].plot(p, quantile)
ax[2].set_xlabel("p")
ax[2].set_ylabel("Q(p)")
ax[2].set_title("Quantile function")
ax[2].grid(alpha=0.25)

plt.tight_layout()

plt.savefig("Uniform_PDF_CDF_Quantile.png", dpi=300)
plt.show()

# One probability
probability = rv.cdf(27)
print("P(X <= 27) =", probability)

# One quantile
x90 = rv.ppf(0.90)
print("90th percentile =", x90)
