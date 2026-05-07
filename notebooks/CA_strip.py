import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(35)
data = rng.integers(0, 2, 20)
plt.rcParams['image.cmap'] = 'binary'
fig, ax = plt.subplots(figsize=(12, 2))

ax.matshow(data[np.newaxis, :])

ax.set_xticks(np.arange(-0.5, len(data), 1), minor=True)
ax.set_yticks(np.arange(-0.5, 1, 1), minor=True)

ax.grid(which='minor')
ax.set_xticks([])
ax.set_yticks([])
ax.tick_params(which='both',
               bottom=False,
               top=False,
               left=False,
               right=False,
               labelbottom=False,
               labelleft=False)
plt.tight_layout()
plt.savefig("CA_strip.png", dpi=300)