"""Classical laminate theory (CLT) for the TMMV64 final project.

Units: use any consistent set, e.g. Pa and m (N in N/m, M in N) or psi and in (N in lb/in, M in lb).
Angles in degrees, measured from the laminate x axis to the fibre direction.
Ply 1 is the bottom ply (most negative z); z is measured from the mid-plane.
Strains use engineering shear: [eps_x, eps_y, gamma_xy].

    Q = ply_stiffness(E1, E2, G12, nu12)
    ABD, abd_inv, z = abd(Q, [0, 90, 90, 0], 0.125e-3)
    # [eps0; kappa] = abd_inv @ [Nx, Ny, Nxy, Mx, My, Mxy]
"""
import numpy as np


def ply_stiffness(E1, E2, G12, nu12):
    """Reduced stiffness Q of one ply in its material axes (3x3)."""
    nu21 = nu12 * E2 / E1
    d = 1 - nu12 * nu21
    return np.array([[E1 / d, nu12 * E2 / d, 0],
                     [nu12 * E2 / d, E2 / d, 0],
                     [0, 0, G12]])


def rotate(Q, theta):
    """Stiffness Qbar of a ply at angle theta (degrees), in laminate axes (3x3)."""
    c, s = np.cos(np.radians(theta)), np.sin(np.radians(theta))
    T = np.array([[c * c, s * s, 2 * c * s],
                  [s * s, c * c, -2 * c * s],
                  [-c * s, c * s, c * c - s * s]])  # stress transformation, laminate -> ply axes
    R = np.diag([1, 1, 2])  # engineering shear <-> tensor shear
    return np.linalg.inv(T) @ Q @ R @ T @ np.linalg.inv(R)


def abd(Q, angles, thicknesses):
    """ABD matrix (6x6), its inverse (6x6) and the ply interfaces z_0..z_N.

    Q: ply stiffness from ply_stiffness (same material in every ply).
    angles: ply angles in degrees, bottom ply first.
    thicknesses: one value per ply, or a single value for all plies.
    """
    t = np.broadcast_to(np.asarray(thicknesses, float), np.shape(angles))
    z = np.concatenate([[0.0], np.cumsum(t)])
    z -= z[-1] / 2
    ABD = np.zeros((6, 6))
    for k, theta in enumerate(angles):
        Qbar = rotate(Q, theta)
        ABD[:3, :3] += Qbar * (z[k + 1] - z[k])
        ABD[:3, 3:] += Qbar * (z[k + 1] ** 2 - z[k] ** 2) / 2
        ABD[3:, 3:] += Qbar * (z[k + 1] ** 3 - z[k] ** 3) / 3
    ABD[3:, :3] = ABD[:3, 3:]
    return ABD, np.linalg.inv(ABD), z


if __name__ == "__main__":
    # Self-check on a [0/90]s laminate: A11 = A22 = 2t(Q11 + Q22), A16 = 0, B = 0.
    Q = ply_stiffness(181e9, 10.3e9, 7.17e9, 0.28)
    t = 0.125e-3
    ABD, abd_inv, z = abd(Q, [0, 90, 90, 0], t)
    assert np.isclose(ABD[0, 0], 2 * t * (Q[0, 0] + Q[1, 1]))
    assert np.isclose(ABD[0, 0], ABD[1, 1]) and abs(ABD[0, 2]) < 1e-6 * ABD[0, 0]
    assert np.allclose(ABD[:3, 3:], 0, atol=1e-9 * ABD[0, 0])
    assert np.allclose(ABD @ abd_inv, np.eye(6))
    np.set_printoptions(precision=4)
    print("[0/90]s, t = 0.125 mm per ply. A (N/m):\n", ABD[:3, :3], "\nD (N m):\n", ABD[3:, 3:])
