# Ag-MB-SERS-Electrochem


## Overview

This repository accompanies a study of the electrochemical and surface-enhanced Raman spectroscopic (SERS) behavior of methylene blue at silver electrodes.

The study combines experimental electrochemistry and potential-dependent Raman spectroscopy with quantum-chemical calculations and electromagnetic simulations. The aim is to examine how electrode potential, the molecular environment, and local electromagnetic field enhancement contribute to the observed spectroscopic behavior.

The repository provides calculation inputs and outputs, experimental data and analyses, and simulation files to support transparency, reproducibility, and independent assessment of the results.

## Scientific approach

The study brings together three complementary approaches:

Experimental electrochemistry and Raman spectroscopy. Cyclic voltammetry and potential-dependent SERS measurements are used to investigate methylene blue at silver electrodes. The experimental documentation includes information on the electrode system, electrolyte, potential reference, and measurement conditions.

Quantum-chemical calculations. TURBOMOLE calculations are used to examine molecular and silver–methylene blue models, their electronic structures, and vibrational properties. Available calculation files include input settings, molecular coordinates, orbital information, and relevant output files. Singlet-state stability analyses and triplet-state calculations are archived separately.

Electromagnetic simulations. MEEP simulations are used to investigate the local electric-field response of simplified silver nanostructures at the Raman excitation wavelength. These calculations help illustrate possible electromagnetic contributions to SERS enhancement.

The three approaches provide complementary information; agreement in one area does not, by itself, establish a unique molecular structure, electronic state, or enhancement mechanism.

## Repository contents

The repository is organized by data type and computational method.

## Experimental data

Experimental voltammetry and Raman data, together with relevant processing and analysis files, are intended to document the measurements and the basis of the reported spectral comparisons.

## TURBOMOLE

The TURBOMOLE directory contains quantum-chemical calculation files and documentation. Its subdirectories distinguish individual calculations, including:

Singlet-state reference calculations.

Singlet SCF stability analysis.

Triplet-state calculations for the Ag40–MB+ model.

Raman calculations for the Ag40–MB+ model.

Each calculation directory includes a README describing its contents and, where relevant, limitations of the corresponding results.

Some large orbital and Raman-related files are stored as ZIP archives. The Raman archive rman_a.zip is supplied in two parts; instructions for reconstructing it are provided in the corresponding calculation directory.

## MEEP

The MEEP calculations investigate electric-field distributions in idealized silver nanostructures, including a nanoparticle dimer and a 2 × 2 array. The simulations are intended to provide a qualitative and model-dependent assessment of electromagnetic hotspot formation.

Numerical comparisons at selected monitoring points should not be interpreted as proof of convergence of an entire field map unless that convergence has been demonstrated separately.

## Interpretation and limitations

The computational models are simplified representations of the experimental electrode surface and molecular environment.

Completion of a quantum-chemical calculation does not automatically establish electronic-state stability or confirm that an optimized geometry is a local minimum. These properties require appropriate stability and vibrational analyses.

Likewise, electromagnetic field enhancements calculated for idealized nanostructures are not direct measurements of experimental SERS enhancement factors.

Experimental spectral comparisons should be interpreted in the context of the measurement conditions, data-processing methods, and limitations described in the associated manuscript.

## Reproducibility and data availability

The repository is intended to preserve the underlying data, computational settings, scripts, and results needed to inspect and reproduce the reported analyses.

For individual calculations, consult the README in the relevant subdirectory before reusing the files. Large archives may need to be extracted or reconstructed first.

The availability and completeness of individual datasets should be checked against the repository contents and the data-availability statement in the final published manuscript.

## Citation

If you use data, scripts, or calculations from this repository, please cite the associated research article once its final bibliographic details are available. A version-specific archival DOI should also be cited where applicable.
