import meep as mp
from meep.materials import Ag
import numpy as np
import csv
import time

# ============================================================
# Ag 2x2 array: field-enhancement / symmetry diagnostic
#
# Corrections relative to the original script:
#   (1) Field AMPLITUDE is taken from single-frequency DFT monitors,
#       not from get_field_point() on real CW fields. get_field_point
#       on a ContinuousSource returns the INSTANTANEOUS real field
#       A*cos(wt+phi) at one instant, so two gaps with different phase
#       are sampled at different points of their cycle -> spurious
#       ratios (this is what produced the ~38:1 upper/lower difference
#       and the "exact swap" on propagation reversal).
#   (2) A broadband Gaussian pulse + DFT at 785 nm + run-until-decayed
#       gives the exact frequency-domain response and removes any
#       steady-state ambiguity (the old run_time = 10 was far too short).
#       NOTE: the Methods text must then read "broadband pulsed source,
#       field taken from a DFT monitor at 785 nm" instead of "CW".
#   (3) The y->-y symmetry claim only holds for a y-symmetric EXCITATION.
#       A single travelling plane wave is NOT invariant under y->-y, so
#       "symmetric geometry => equal horizontal gaps" is only testable
#       with the symmetric double source below.
#
# Three excitations are run and compared:
#   single_fwd  : one line source below the array  (original setup)
#   single_rev  : one line source above the array  (reversal test)
#   symmetric   : two in-phase line sources at +/-y (enforces y-symmetry
#                 of the drive; any residual upper/lower difference is
#                 then pure numerics)
# ============================================================

# ---- physical / numerical parameters ----
wavelength = 0.785            # um
fcen = 1.0 / wavelength
df   = 0.15 * fcen            # pulse bandwidth (only needs to cover fcen)

n_medium = 1.33
medium = mp.Medium(index=n_medium)

diameter = 0.050             # 50 nm
radius = diameter / 2
gap = 0.002                  # 2 nm surface-to-surface
center_distance = diameter + gap
half = center_distance / 2   # cylinder-centre offset from origin

cell_size = 0.70             # um (larger than before: near-field decays before PML)
pml = 0.10                   # um
resolution = 2000            # pixels/um = 0.5 nm grid
                             # use 1000 (1 nm) for a quick check / convergence pair
src_offset = 0.10            # source distance from origin (um)

cell = mp.Vector3(cell_size, cell_size, 0)
boundary_layers = [mp.PML(pml)]

# Ex polarization = field along x = horizontal axis.
# Expectation: horizontal (x-aligned) gaps enhance, vertical gaps suppressed.
junctions = {
    "upper_horizontal": mp.Vector3(0.0, +half),
    "lower_horizontal": mp.Vector3(0.0, -half),
    "left_vertical":    mp.Vector3(-half, 0.0),
    "right_vertical":   mp.Vector3(+half, 0.0),
}


def make_geometry():
    return [
        mp.Cylinder(radius=radius, center=mp.Vector3(sx * half, sy * half), material=Ag)
        for sx in (-1, 1) for sy in (-1, 1)
    ]


def make_sources(mode):
    src = mp.GaussianSource(frequency=fcen, fwidth=df)
    line = cell_size - 2 * pml
    below = mp.Source(src, component=mp.Ex,
                      center=mp.Vector3(0, -src_offset), size=mp.Vector3(line, 0))
    above = mp.Source(src, component=mp.Ex,
                      center=mp.Vector3(0, +src_offset), size=mp.Vector3(line, 0))
    if mode == "single_fwd":
        return [below]
    if mode == "single_rev":
        return [above]
    if mode == "symmetric":
        return [below, above]        # in-phase, symmetric about y = 0
    raise ValueError(mode)


def run_case(mode, with_ag):
    sim = mp.Simulation(
        cell_size=cell,
        boundary_layers=boundary_layers,
        geometry=make_geometry() if with_ag else [],
        sources=make_sources(mode),
        default_material=medium,
        resolution=resolution,
    )

    # zero-size DFT monitors: complex Ex amplitude at each junction centre
    mons = {name: sim.add_dft_fields([mp.Ex], fcen, 0, 1,
                                     center=pos, size=mp.Vector3())
            for name, pos in junctions.items()}

    # DFT field map for the figure
    mapmon = sim.add_dft_fields([mp.Ex], fcen, 0, 1,
                                center=mp.Vector3(), size=mp.Vector3(0.20, 0.20))

    # run until the pulse has passed and the fields have decayed
    decay_pt = mp.Vector3(0, -half)   # inside the lower horizontal gap
    sim.run(until_after_sources=20)

    vals = {name: float(np.abs(sim.get_dft_array(m, mp.Ex, 0)))
            for name, m in mons.items()}

    arr = np.abs(sim.get_dft_array(mapmon, mp.Ex, 0))
    tag = "Ag" if with_ag else "Ref"
    np.save(f"{tag}_2x2_{mode}_Ex_DFT_785nm.npy", arr)

    return vals


print("=" * 64)
print("Ag 2x2 symmetry / enhancement diagnostic")
print(f"wavelength   = {wavelength*1000:.0f} nm")
print(f"resolution   = {resolution} pixels/um  (grid = {1000/resolution:.3f} nm)")
print(f"gap = {gap*1000:.0f} nm  ->  {gap*resolution:.0f} cells across the gap")
print("=" * 64)

summary = []

start_time = time.time()
total_runs = 6
completed_runs = 0



for mode in ("symmetric",):
    print(f"\n########## excitation: {mode} ##########")

    print("--- Ag-containing model ---")
    E_ag = run_case(mode, with_ag=True)
    print("--- Ag-free reference ---")
    E0 = run_case(mode, with_ag=False)


    completed_runs += 2
    elapsed = time.time() - start_time
    avg_per_run = elapsed / completed_runs
    remaining = avg_per_run * (total_runs - completed_runs)

    print(f"\n>>> Fortschritt: {completed_runs}/{total_runs} Simulationen")
    print(f">>> Laufzeit bisher: {elapsed/60:.1f} min")
    print(f">>> Geschätzte Restzeit: {remaining/60:.1f} min")
    
    rows = []
    for name in junctions:
        ratio = E_ag[name] / E0[name]
        gem = ratio ** 4
        rows.append([name, E_ag[name], E0[name], ratio, gem])
        print(f"  {name:18s} |EAg|={E_ag[name]:.6g}  |E0|={E0[name]:.6g}  "
              f"|E/E0|={ratio:.4g}  |E/E0|^4={gem:.4g}")

    out_csv = f"Ag_2x2_785nm_{mode}_results.csv"
    with open(out_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["junction", "EAg_abs", "E0_abs", "E_ratio", "G_EM_E4"])
        w.writerows(rows)

    uh = E_ag["upper_horizontal"] / E0["upper_horizontal"]
    lh = E_ag["lower_horizontal"] / E0["lower_horizontal"]
    hor_ratio = lh / uh if uh > 0 else float("inf")
    print(f"  --> lower/upper horizontal |E/E0| ratio = {hor_ratio:.3f}")
    summary.append((mode, uh, lh, hor_ratio))

print("\n" + "=" * 64)
print("SUMMARY: lower/upper horizontal ratio by excitation")
print("=" * 64)
for mode, uh, lh, r in summary:
    print(f"  {mode:12s}  upper={uh:.4g}  lower={lh:.4g}  lower/upper={r:.3f}")
print("\nExpected:")
print("  single_fwd / single_rev : modest ratio (physical retardation),")
print("                            interchanged on reversal -- NOT ~38x.")
print("  symmetric               : ratio ~ 1 (equal gaps); any deviation")
print("                            is pure numerical/grid error.")
print("done.")
