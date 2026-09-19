# Raman calculation: Ag40-MB+

This folder contains the TURBOMOLE files for the Raman calculation of the Ag40-MB+ model.

## Calculation files

Geometry: coord

Settings: control

Basis sets: basis, auxbasis

SCF results: energy, ridft.out

Vibrations: aoforce.out, hessian, vib_normal_modes, vibrational_dipols, vibspectrum

## Raman results: egrad.out, intense.out, dipgrad

The large files alpha, beta, rman_a and dipl_a are supplied as separate ZIP archives. Extract them before reuse.

The Excel file, PNG figure and Word document contain supplementary Raman analyses.

## Limitations

Completed calculations do not automatically prove that the geometry is a local minimum or that the electronic state is stable. These questions require separate checks.

## Reconstructing the Raman archive

The original rman_a.zip was split into two parts to meet GitHub's web-upload size limit.

Download rman_a.zip.part1 and rman_a.zip.part2 into the same directory.

Open Windows PowerShell in that directory and run:

```powershell
$parts = @("rman_a.zip.part1", "rman_a.zip.part2")
```

$parts = @("rman_a.zip.part1", "rman_a.zip.part2")
$out = [IO.File]::Create("rman_a.zip")
try {
    foreach ($part in $parts) {
        $inputFile = [IO.File]::OpenRead($part)
        try {
            $inputFile.CopyTo($out)
        }
        finally {
            $inputFile.Dispose()
        }
    }
}
finally {
    $out.Dispose()
}

The resulting rman_a.zip can then be extracted to restore the original rman_a file.
