# MEEP grid-convergence calculation: 0.5 nm

This directory contains the 0.5 nm grid-spacing calculation for the symmetric 2 × 2 Ag nanoparticle arrangement.

Simulation parameters:
- Excitation wavelength: 785 nm
- Ag particle diameter: 50 nm
- Interparticle gap: 2 nm
- Grid spacing: 0.5 nm
- Surrounding medium: refractive index 1.33

The symmetric calculation gives electric-field enhancement factors of 8.581 at both the upper and lower horizontal gap-center monitor points.

The corresponding 1.0 nm calculation gives 8.621 at both points. The relative difference is approximately 0.46%.

This comparison demonstrates agreement at the selected monitor points. It does not establish convergence of the complete spatial field distribution.

The calculation script, numerical results, field arrays, and execution log are archived alongside this README.
