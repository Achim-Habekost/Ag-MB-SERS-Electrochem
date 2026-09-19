# Triplet calculation: Ag40–MB+

This directory archives the TURBOMOLE calculation files for the triplet-state Ag40–MB+ model discussed in the manuscript.

The original calculation output is retained, including its warning about a negative HOMO–LUMO gap. Completion of the calculation does not by itself establish electronic-state stability.

The alpha and beta orbital files are provided separately as ZIP archives and must be extracted before reuse.

# Archived calculation files

The archive contains the TURBOMOLE input and output files for the Ag40–MB+ triplet calculation, including the molecular coordinates (coord), computational settings (control), basis-set definitions (basis, auxbasis), SCF results (energy, ridft.out), and vibrational-analysis results (aoforce.out, hessian, vib_normal_modes, vibspectrum).

Additional files document the gradient and intensity calculations. The alpha.zip and beta.zip archives contain the corresponding orbital files.

# Interpretation and limitations

The original SCF output reports a negative HOMO–LUMO gap of approximately −0.0635 eV and explicitly warns that the orbital occupations should be checked. This result must not be interpreted as evidence that the triplet state is electronically stable.

The vibrational calculation was completed, but the presence of negative frequencies requires separate assessment. Completion of the vibrational analysis does not establish that the structure is a local minimum.

The archived files are provided to make the calculations reproducible and to document these limitations transparently. A definitive comparison of singlet and triplet stability requires examination of the electronic occupations, the relevant total energies at consistent geometries and computational settings, and the vibrational results.
