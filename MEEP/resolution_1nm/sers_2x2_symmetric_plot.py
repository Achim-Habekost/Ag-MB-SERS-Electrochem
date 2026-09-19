import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.colors import LogNorm

# ------------------------------------------------------------
# Symmetric 2x2 Ag array, 785 nm
# DFT-based field enhancement, 1 nm grid
# ------------------------------------------------------------

E_ag = np.load("Ag_2x2_symmetric_Ex_DFT_785nm.npy")
E_0  = np.load("Ref_2x2_symmetric_Ex_DFT_785nm.npy")

# Avoid division by zero
eps = 1e-12

# Point-by-point normalization
F = np.abs(E_ag) / np.maximum(np.abs(E_0), eps)

# Electromagnetic SERS approximation
G = F**4

print("Array shape:", G.shape)
print("Max |E/E0| =", np.nanmax(F))
print("Max |E/E0|^4 =", np.nanmax(G))

# The DFT arrays cover 0.2 x 0.2 um = 200 x 200 nm
extent = [-100, 100, -100, 100]

# Limit the displayed range to avoid source/PML regions
G_plot = np.clip(G, 1.0, 1e4)

fig, ax = plt.subplots(figsize=(7.4, 6.3))

im = ax.imshow(
    G_plot.T,
    origin="lower",
    extent=extent,
    cmap="viridis",
    norm=LogNorm(vmin=1, vmax=1e4),
    interpolation="nearest",
    aspect="equal"
)

# ------------------------------------------------------------
# Four Ag nanostructures
# diameter = 50 nm, gap = 2 nm
# centers at +/-26 nm in x and y
# ------------------------------------------------------------

particle_centers = [
    (-26,  26),
    ( 26,  26),
    (-26, -26),
    ( 26, -26)
]

for x, y in particle_centers:
    circle = Circle(
        (x, y),
        radius=25,
        fill=False,
        linewidth=1.5,
        edgecolor="black"
    )
    ax.add_patch(circle)

# Focus on the physically relevant array region
ax.set_xlim(-70, 70)
ax.set_ylim(-70, 70)

ax.set_xlabel("x / nm")
ax.set_ylabel("y / nm")
ax.set_title(
    "Ag 2x2 array, 785 nm: symmetric excitation\n"
    r"EM-SERS enhancement $|E/E_0|^4$"
)

cbar = fig.colorbar(im, ax=ax, pad=0.04)
cbar.set_label(r"$|E/E_0|^4$")

plt.tight_layout()

outfile = "Ag_2x2_785nm_symmetric_DFT_SERS_E4.png"
plt.savefig(outfile, dpi=300, bbox_inches="tight")

print("Saved:", outfile)

plt.show()
