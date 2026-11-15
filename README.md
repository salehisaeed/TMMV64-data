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
| `hw2/kelmarsh_t1_2016-2017.csv` | 5.7 MB |
| `hw2/bearing_cwru_12k.npz` | 6.0 MB |

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
