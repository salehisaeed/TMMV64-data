# TMMV64 data

Data files for the homework of **TMMV64 Machine Learning for Mechanical Engineering**, Linköping University.
The course notebooks download them from here. Each file below names its source; please cite the source, not this
repository, when you use the data.

## hw1: cylinder wake at Re = 1000

| File | Size |
|:--|--:|
| `hw1/cylinder_Re1000_fine_velocity.npz` | 83 MB |
| `hw1/cylinder_Re1000_fine_vorticity.npz` | 45 MB |

A two-dimensional simulation of the flow past a circular cylinder at Reynolds number 1000 (OpenFOAM, diameter 1,
inflow speed 1): 201 snapshots from t = 70 to 120 with a step of 0.25, on the 58 582 mesh cells with x ≤ 14
diameters. The velocity components u, v are in one file, the vorticity in the other; the values are the cell values
of the simulation, with the cell centers, areas and a triangulation for plotting. Being two-dimensional, this is a
periodic laminar wake.

Source: Saeed Salehi, Linköping University (simulation made for this course). License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## hw2: wind turbine and bearing vibration

| File | Size |
|:--|--:|
| `hw2/kelmarsh_t1_2016-2017.npz` | 1.3 MB |
| `hw2/kelmarsh_t1_2016-2017.csv` | 5.7 MB |
| `hw2/bearing_cwru_12k.npz` | 6.0 MB |

**`kelmarsh_t1_2016-2017.npz`** (used by the notebook): the records of the CSV file below that have a wind speed and a
power, as NumPy arrays (year, month, wind, power, pitch, rotor_speed, t_ambient, wind_direction), with a status for
each record: `clean` (running normally), `curtailed` (running, but the power limited by the grid operator), `warning`,
`stop` or `low wind`. Same source and license as the CSV file.

**`kelmarsh_t1_2016-2017.csv`**: ten-minute records of turbine 1 of the Kelmarsh wind farm (England) for 2016 and
2017: wind speed, power, pitch angle, rotor speed, ambient temperature, wind direction and the logged state of the
turbine. A reduced copy (one turbine, two years, eight columns) of the original data.

Source: Plumley, C. and Takeuchi, R., *Kelmarsh wind farm data*, Zenodo, version 4 (2025),
[doi:10.5281/zenodo.16807551](https://doi.org/10.5281/zenodo.16807551). License: CC BY 4.0. Changes: the records of
one turbine and two years were selected and the columns renamed.

**`bearing_cwru_12k.npz`**: vibration of a motor bearing (drive-end bearing SKF 6205, accelerometer at the drive end,
12 kHz), healthy and with seeded faults of three kinds (inner race, ball, outer race at 6 o'clock), fault diameters
0.007, 0.014 and 0.021 inch, motor loads 0 to 3 hp: 40 recordings, the first 5 s of each. The healthy recordings,
made at 48 kHz, were decimated to 12 kHz.

Source: Case Western Reserve University Bearing Data Center,
[engineering.case.edu/bearingdatacenter](https://engineering.case.edu/bearingdatacenter). A reduced copy of their
data, shared here for teaching with credit to the Bearing Data Center. For the original data and more information,
see their website. It will be removed on request.

## hw3: airfoil self-noise and steel plate faults

| File | Size |
|:--|--:|
| `hw3/airfoil_self_noise.npz` | 9 kB |
| `hw3/steel_plates_faults.npz` | 131 kB |

**`airfoil_self_noise.npz`**: the noise of NACA 0012 blade sections in the anechoic wind tunnel of NASA Langley,
1503 one-third-octave bands of 106 measured spectra. Arrays: frequency (Hz), angle (angle of attack, degrees), chord
(m), speed (flow speed, m/s), thickness (suction-side displacement thickness at the trailing edge, m), noise (scaled
sound pressure level, dB), and spectrum (the number of the measured spectrum, 0 to 105, one per chord, speed and
angle, added here).

Source: T. F. Brooks, D. S. Pope and M. A. Marcolini, *Airfoil self-noise and prediction*, NASA Reference
Publication 1218 (1989). Data: Brooks, T., Pope, D. and Marcolini, M., *Airfoil Self-Noise*, UCI Machine Learning
Repository (1989), [doi:10.24432/C5VW2C](https://doi.org/10.24432/C5VW2C). License: CC BY 4.0. Changes: the columns
stored as named arrays; the spectrum number added.

**`steel_plates_faults.npz`**: 1941 surface faults of steel plates, each described by 27 measured numbers (features,
with their names in names) and its kind (kind, one of the seven in kinds: pastry, Z scratch, K scratch, stains,
dirtiness, bumps, other).

Source: Buscema, M., Terzi, S. and Tastle, W., *Steel Plates Faults*, UCI Machine Learning Repository (2010),
[doi:10.24432/C5J88N](https://doi.org/10.24432/C5J88N); Semeion Research Center of Sciences of Communication, Rome.
License: CC BY 4.0. Changes: the seven indicator columns of the kind stored as one array of names.

## projects/turbofan: turbofan engine degradation (NASA C-MAPSS)

| File | Size |
|:--|--:|
| `projects/turbofan/CMAPSSData.zip` | 12 MB |

**`CMAPSSData.zip`**: simulated run-to-failure data of a fleet of turbofan engines, four subsets (FD001 to FD004: one
or six operating conditions, one or two fault modes). For each subset, `train_FD00k.txt` (engines run until failure),
`test_FD00k.txt` (engines stopped some time before failure) and `RUL_FD00k.txt` (the true remaining life of each test
engine); text files with 26 columns (engine, cycle, three operational settings, 21 sensors). NASA's `readme.txt` is
included.

Source: A. Saxena and K. Goebel, *Turbofan Engine Degradation Simulation Data Set*, NASA Prognostics Data Repository,
NASA Ames Research Center (2008),
[nasa.gov/.../pcoe-data-set-repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/).
The data are described in A. Saxena, K. Goebel, D. Simon and N. Eklund, *Damage propagation modeling for aircraft
engine run-to-failure simulation*, PHM08, Denver (2008). NASA states no license; it asks users to acknowledge the
repository and the donors of the data. A copy of NASA's data files (without the paper that NASA's zip file also
holds), kept here so that the course does not depend on the original address. It will be removed on request.

## projects/woven: elastic properties of unidirectional and woven composites

| File | Size |
|:--|--:|
| `projects/woven/ElasEngCoefDataSet.xlsx` | 0.3 MB |

**`ElasEngCoefDataSet.xlsx`**: finite element results of representative volume elements of composites. The sheet
`400DataPoints` holds 400 Sobol samples of five inputs (matrix modulus and Poisson's ratio, fiber modulus and
Poisson's ratio, fiber volume fraction `phiF`; moduli in MPa) and, for each, the engineering constants of a 3D
unidirectional RVE with random fibers (1 = fiber direction) and four properties of a plain-weave ply (Ex, Ey, Gxy in
GPa, and νxy). Reading it with pandas needs `openpyxl`.

Source: E. Ghane, M. Fagerström and S. M. Mirkhalaf, *A multiscale deep learning model for elastic properties of
woven composites*, International Journal of Solids and Structures 282 (2023) 112452,
[doi:10.1016/j.ijsolstr.2023.112452](https://doi.org/10.1016/j.ijsolstr.2023.112452). The authors' file, unchanged,
from their repository [github.com/EsanGhaneh/MultiscaleElasticWovenNeuralNet](https://github.com/EsanGhaneh/MultiscaleElasticWovenNeuralNet).
License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); please cite the paper.

## projects/laminate: classical laminate theory

| File | Size |
|:--|--:|
| `projects/laminate/clt.py` | 2 kB |

**`clt.py`**: classical laminate theory in Python (NumPy): the reduced stiffness of a ply, its rotation, and the ABD
matrix of a laminate with its inverse. Code, not data: download it next to your notebook and `import clt`.

Source: Ehsan Ghane, written for this course (TMMV64, Linköping University).
