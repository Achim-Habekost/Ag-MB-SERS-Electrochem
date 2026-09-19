import meep as mp
from meep.materials import Ag

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# SERS Ag-Dimer: Grundparameter
# -----------------------------------------

wavelength = 0.785       # µm = 785 nm
frequency = 1 / wavelength

n_medium = 1.33          # ca. 0.1 M KCl(aq)
eps_medium = n_medium**2

diameter = 0.050         # µm = 50 nm
radius = diameter / 2

gap = 0.002              # µm = 2 nm

print("MEEP SERS-Modell")
print("-----------------")
print(f"Laserwellenlaenge: {wavelength*1000:.0f} nm")
print(f"Frequenz (MEEP):   {frequency:.4f} 1/um")
print(f"Medium n:          {n_medium:.3f}")
print(f"Medium epsilon:    {eps_medium:.4f}")
print(f"Ag-Durchmesser:    {diameter*1000:.0f} nm")
print(f"Spalt:             {gap*1000:.1f} nm")
print("Ag-Materialmodell erfolgreich geladen.")


# -----------------------------------------
# Ag-Dimer-Geometrie
# -----------------------------------------

center_distance = diameter + gap

geometry = [
    mp.Cylinder(
        radius=radius,
        center=mp.Vector3(-center_distance/2, 0),
        material=Ag
    ),
    mp.Cylinder(
        radius=radius,
        center=mp.Vector3(+center_distance/2, 0),
        material=Ag
    )
]

print()
print("Ag-Dimer erzeugt.")
print(f"Mittelpunktabstand: {center_distance*1000:.1f} nm")
print(f"Spaltbreite: {gap*1000:.1f} nm")


# -----------------------------------------
# Simulationszelle und 785-nm-Lichtquelle
# -----------------------------------------

cell_size = 0.40         # µm
pml = 0.1                # µm

cell = mp.Vector3(cell_size, cell_size, 0)

boundary_layers = [
    mp.PML(pml)
]

medium = mp.Medium(index=n_medium)

sources = [
    mp.Source(
        mp.ContinuousSource(frequency=frequency),
        component=mp.Ex,
        center=mp.Vector3(0, -0.08),
        size=mp.Vector3(cell_size - 2*pml, 0)
    )
]

print()
print("Simulationszelle definiert.")
print("Laser: 785 nm")
print("Polarisation: Ex")
print("Ausbreitung: y-Richtung")
print("E-Feld parallel zur Ag-Ag-Achse.")


# -----------------------------------------
# MEEP-Simulation
# -----------------------------------------

resolution = 1000        # Pixel/um = 1 nm pro Gitterzelle

sim = mp.Simulation(
    cell_size=cell,
    boundary_layers=boundary_layers,
    geometry=geometry,
    sources=sources,
    default_material=medium,
    resolution=resolution
)

print()
print("MEEP-Simulation erzeugt.")
print(f"Aufloesung: {resolution} Pixel/um")
print(f"Gitterabstand: {1000/resolution:.1f} nm")

# -----------------------------------------
# Feldberechnung starten
# -----------------------------------------

print()
print("Starte FDTD-Rechnung ...")

dft = sim.add_dft_fields(
    [mp.Ex],
    frequency,
    0,
    1,
    center=mp.Vector3(),
    size=mp.Vector3(0.2, 0.2)
)

sim.run(until=10)

# -----------------------------------------
# Feldkarte erzeugen
# -----------------------------------------

ex = sim.get_dft_array(dft, mp.Ex, 0)

field = np.abs(ex)

np.save("Ag_Dimer_Ex_DFT_785nm.npy", field)

fig, ax = plt.subplots(figsize=(8, 7))

im = ax.imshow(
    field.T,
    origin="lower",
    extent=[-100, 100, -100, 100],
    aspect="equal"
)

# Ag-Partikel als Kreise einzeichnen
circle1 = plt.Circle((-26, 0), 25, fill=False, linewidth=1.5)
circle2 = plt.Circle((26, 0), 25, fill=False, linewidth=1.5)

ax.add_patch(circle1)
ax.add_patch(circle2)

ax.set_xlabel("x / nm")
ax.set_ylabel("y / nm")
ax.set_title("Ag-Dimer, 785 nm: |Ex|")

plt.colorbar(im, ax=ax, label="|Ex| (MEEP units)")

plt.savefig("Ag_Dimer_785nm_DFT_Feld.png", dpi=300, bbox_inches="tight")

plt.close()

print()
print("Feldkarte gespeichert:")
print("Ag_Dimer_785nm_DFT_Feld.png")


E_gap = sim.get_field_point(mp.Ex, mp.Vector3(0, 0))

np.save("Referenz_E0_DFT_785nm.npy", np.array([abs(E_gap)]))

print()
print("Elektrisches Feld im Spaltzentrum:")
print("Ex =", E_gap)
print("|Ex| =", abs(E_gap))

print("FDTD-Rechnung beendet.")
