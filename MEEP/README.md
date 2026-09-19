# MEEP simulations

This directory contains MEEP finite-difference time-domain (FDTD) simulations associated with the Ag–methylene blue SERS study.

The simulations investigate electromagnetic near-field enhancement at 785 nm for:
- An Ag nanoparticle dimer with a 2 nm gap.
- A symmetric 2 × 2 arrangement of Ag nanoparticles with 2 nm gaps.

The 2 × 2 model includes calculations at grid spacings of 1.0 nm and 0.5 nm. The grid comparison assesses the electric-field enhancement at selected gap-center monitor points; convergence of the complete field map has not been established.

Simulation scripts, input parameters, numerical results, and figures will be provided in this directory.

The models describe idealized two-dimensional Ag structures and do not represent the complete experimental electrode morphology or its potential-dependent AgCl composition.

## Ag dimer simulation: archived files

The Ag dimer simulation investigates electromagnetic near-field enhancement at an excitation wavelength of 785 nm for an idealized silver dimer with a 2 nm gap.

The following files are archived in this directory:

sers_ag.py — MEEP simulation script.

Ag_Dimer_Ex_DFT_785nm.npy — calculated electric-field data for the Ag dimer.

Referenz_Ex_DFT_785nm.npy — corresponding reference-field data.

Ag_Dimer_785nm_SERS_E4.png — visualization of the calculated fourth-power field-enhancement quantity.

The field-enhancement results are based on the simulated electric field relative to the reference field. The fourth-power quantity is an electromagnetic approximation and should not be interpreted as an experimentally measured absolute SERS enhancement factor.

The model represents an idealized two-dimensional Ag geometry rather than the complete morphology or chemical composition of the experimental electrode.
