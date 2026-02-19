# utils_holprt_main_optimized.py
# Strategy A + GS (your working algorithm), but optimized / de-duplicated
import os, re
import numpy as np
from utils_holprt import *

# ============================================================
# Small utilities
# ============================================================
import traceback

def _resolve_path(p, base_dir=None):
    """Return p if it exists; else try base_dir/p."""
    if p is None:
        return p
    if file_exists(p):
        return p
    if base_dir is not None:
        q = os.path.join(base_dir, p)
        if file_exists(q):
            return q
    return p  # let downstream throw a clear error if missing


def print_debug(fout, var):
    # 1. Extract variable name from source code
    stack = traceback.extract_stack()
    _, _, _, text = stack[-2]
    # find the text after the last comma inside the parentheses
    args_str = text[text.find('(')+1 : text.rfind(')')]
    var_name = args_str.split(',')[-1].strip()

    # 2. Get basic info
    var_type = type(var).__name__
    info_str = ""

    # 3. Handle specific types
    if isinstance(var, np.ndarray):
        info_str = f" | Shape: {var.shape}"

    elif isinstance(var, list):
        # Calculate dimensions for nested lists
        dims = []
        curr = var
        while isinstance(curr, list):
            dims.append(len(curr))
            curr = curr[0] if len(curr) > 0 else None
        info_str = f" | Dims: {tuple(dims)}"

    elif isinstance(var, dict):
        # For dicts, show the count and the keys
        keys_list = list(var.keys())
        info_str = f" | Size: {len(var)} keys | Keys: {keys_list}"

    # 4. Write to file
    fout.write(f"DEBUG: {var_name} | Type: {var_type}{info_str} | Value: {var}\n")


def _collect_needed_cmos(list_adiabs, ihole, ipart):
    """Return sorted unique CMO indices needed for these adiabatic states."""
    needed = set()
    for K in list_adiabs:
        ist = K - 1
        needed.update(ihole[ist])
        needed.update(ipart[ist])
    return sorted(needed)



# ============================================================
# Linear algebra helpers
# ============================================================

def mgs_orthonormalize_columns(H, eps=1e-12):
    H = np.asarray(H)
    Q = np.zeros_like(H, dtype=H.dtype)
    for i in range(H.shape[1]):
        v = H[:, i].copy()
        for j in range(i):
            proj = np.vdot(Q[:, j], v)
            v -= proj * Q[:, j]
        nrm = np.linalg.norm(v)
        if nrm < eps:
            raise ValueError(f"MGS: linear dependence at column {i}, norm={nrm:.3e}")
        Q[:, i] = v / nrm
    return Q


# ============================================================
# Cube IO + caching
# ============================================================

class CubeCache:
    """
    Cache cube grids by absolute path.
    Optionally can also store structure metadata if you need it later.
    """
    def __init__(self):
        self._grid = {}   # abs_path -> cube grid
        self._meta = {}   # abs_path -> (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm)

    def read_grid(self, cube_path, *, Lnorm=True, L_structure_only=False):
        ap = os.path.abspath(cube_path)
        if (not L_structure_only) and (ap in self._grid):
            return self._grid[ap]
        natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, grid = read_cube_file(
            ap, Lnorm=Lnorm, L_structure_only=L_structure_only
        )
        self._meta[ap] = (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm)
        if not L_structure_only:
            self._grid[ap] = grid
        return grid

    def read_meta(self, cube_path):
        ap = os.path.abspath(cube_path)
        if ap in self._meta:
            return self._meta[ap]
        # force structure-only read
        _ = self.read_grid(ap, Lnorm=False, L_structure_only=True)
        return self._meta[ap]

#def read_cube_file(cube_file, Lnorm=True, L_structure_only=False):
#    debug = False
#    with open(cube_file, "r") as f:
#        file_data = f.readlines()
#
#    natoms = int(file_data[2].split()[0])
#    crdorg = np.array([float(file_data[2].split()[i+1]) for i in range(3)], dtype=float)
#
#    kabc = np.array([int(file_data[i].split()[0]) for i in range(3, 6)], dtype=int)
#    abc = np.array([[float(file_data[i].split()[j+1]) for j in range(3)] for i in range(3, 6)], dtype=float)
#
#    cube_grid = np.zeros((kabc[0], kabc[1], kabc[2]), dtype=float)
#    crdatm = np.zeros((natoms, 3), dtype=float)
#    iatsrl = np.zeros((natoms,), dtype=int)
#
#    for i in range(natoms):
#        parts = file_data[i+6].split()
#        iatsrl[i] = int(parts[0])
#        crdatm[i, :] = np.array(parts[2:5], dtype=float)
#
#    small = 1e-6
#    for iabc in range(3):
#        for ixyz in range(3):
#            if abs(abc[iabc, ixyz]) < small:
#                abc[iabc, ixyz] = 0.0
#
#    abc_grid = abc
#
#    if L_structure_only:
#        return natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, cube_grid
#
#    if kabc[2] % 6 == 0:
#        nlines = kabc[2] // 6
#    else:
#        nlines = kabc[2] // 6 + 1
#
#    line = natoms + 6
#    for ia in range(kabc[0]):
#        for ib in range(kabc[1]):
#            ic = 0
#            for _ in range(nlines):
#                line_data = file_data[line].split()
#                for val in line_data:
#                    cube_grid[ia, ib, ic] = float(val)
#                    ic += 1
#                line += 1
#
#    if Lnorm:
#        dnorm = np.sqrt(np.sum(cube_grid * cube_grid))
#        cube_grid = cube_grid / dnorm
#
#    return natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, cube_grid

#def write_cube_file(filnam, natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, cube_grid, Line2_text):
#    with open(filnam, "w") as f:
#        f.write("Cube file generated by write_cube_file by T. Zeng\n")
#        f.write(Line2_text)
#        f.write("{:4d} {:12.5f} {:12.5f} {:12.5f} \n".format(natoms, *crdorg))
#        for iabc in range(3):
#            f.write("{:4d} {:12.5f} {:12.5f} {:12.5f} \n".format(kabc[iabc], *abc_grid[iabc, 0:3]))
#        for iatom in range(natoms):
#            f.write("{:4d} ".format(iatsrl[iatom]))
#            f.write("{:12.5f} {:12.5f} {:12.5f} {:12.5f} \n".format(0.0, *crdatm[iatom, 0:3]))
#
#        if kabc[2] % 6 == 0:
#            nlines = kabc[2] // 6
#        else:
#            nlines = kabc[2] // 6 + 1
#
#        for ia in range(kabc[0]):
#            for ib in range(kabc[1]):
#                for line in range(nlines):
#                    line_data = cube_grid[ia, ib, line*6:(line+1)*6]
#                    string_to_write = "{:13.5E}" * len(line_data)
#                    f.write(string_to_write.format(*line_data) + "\n")

# ============================================================
# CP2K TDDFT parsing (unchanged, just kept here)
# ============================================================

#def read_cp2k_output(filnam, small=0.1):
#    with open(filnam, "r") as f:
#        filecontent = f.readlines()
#
#    Elist = []
#    nstate = 0
#    cicoef, ihole, ipart = [], [], []
#    line_ind, line_jnd = [], []
#    osc_list = []
#
#    for iline, line in enumerate(filecontent):
#        sp = line.split()
#        if len(sp) == 3 and sp[2] == "eV":
#            line_ind.append(iline)
#            if nstate > 0:
#                line_jnd.append(iline)
#            nstate += 1
#            Elist.append(float(sp[1]))
#
#        if "strength (a.u.)" in line:
#            line_osc = iline + 2
#
#        if "Eigenvalues of the occupied subspace spin            1" in line:
#            line_Eoccorb_begin = iline + 2
#
#        if "Fermi Energy [eV] :" in line:
#            line_Eoccorb_end = iline - 1
#            for jline in range(iline, iline + 10):
#                if "-------" in filecontent[jline]:
#                    line_Evirorb_begin = jline + 1
#                    break
#
#        if len(sp) == 3 and sp[0] == "Total" and sp[1] == "energy:":
#            E_scf = float(sp[2])
#
#    print(f"\nThe number of TDDFT states: {nstate}")
#    # find end marker for last state (guard)
#    for iline in range(line_ind[-1], min(line_ind[-1] + 3000, len(filecontent))):
#        if "-----------------" in filecontent[iline]:
#            line_jnd.append(iline)
#            break
#
#    for istate in range(nstate):
#        hole_list, part_list, ampl_list = [], [], []
#        for line in range(line_ind[istate] + 1, line_jnd[istate]):
#            sp = filecontent[line].split()
#            hole = int(sp[0]); particle = int(sp[1]); amplitude = float(sp[2])
#            if abs(amplitude) > small:
#                hole_list.append(hole)
#                part_list.append(particle)
#                ampl_list.append(amplitude)
#        ihole.append(hole_list)
#        ipart.append(part_list)
#        cicoef.append(ampl_list)
#
#        osc = float(filecontent[istate + line_osc].split()[-1])
#        osc_list.append(osc)
#
#    # orbital energies table
#    Eorb = []
#    for line in range(line_Evirorb_begin, min(line_Evirorb_begin + 100, len(filecontent))):
#        if "*******" in filecontent[line]:
#            line_Evirorb_end = line - 2
#            break
#
#    for line in range(line_Eoccorb_begin, line_Eoccorb_end + 1):
#        Eorb.extend(filecontent[line].split())
#
#    for line in range(line_Evirorb_begin, line_Evirorb_end + 1):
#        Eorb.extend(filecontent[line].split())
#
#    return ihole, ipart, cicoef, osc_list, Eorb, np.array(Elist, dtype=float), E_scf

# ============================================================
# Transition density / NHO-NPO (kept compatible, but faster lookups)
# ============================================================

def trnden_1state(
    holes, parts, cicoef,
    list_read_orbs=None, list_read_cube=None,
    l_get_nhpo_cube=True,
    return_svd=False,
    cmo_dir="."
):
    """
    Same outputs as your version. Optimization:
    - order-preserving unique holes/parts via dict
    - dict cache for list_read_orbs -> index
    """
    if list_read_orbs is None: list_read_orbs = []
    if list_read_cube is None: list_read_cube = []

    # preserve order
    unique_holes = list(dict.fromkeys(holes))
    unique_parts = list(dict.fromkeys(parts))

    cicoef = np.array(cicoef, dtype=float)
    dnorm = np.linalg.norm(cicoef, 2)
    print(f"Norm of CI Coefficients: {dnorm}")
    cicoef_normal = cicoef / dnorm
    assert np.allclose(np.linalg.norm(cicoef_normal, 2), 1.0)

    mhorb = len(unique_holes)
    nporb = len(unique_parts)
    tdm_cmo = np.zeros((mhorb, nporb), dtype=float)

    hole_pos = {h:i for i,h in enumerate(unique_holes)}
    part_pos = {p:i for i,p in enumerate(unique_parts)}
    for h, p, c in zip(holes, parts, cicoef_normal):
        tdm_cmo[hole_pos[h], part_pos[p]] = c

    holnat, sglval, prtnat = np.linalg.svd(tdm_cmo, full_matrices=True)
    prtnat = prtnat.transpose()

    # build local dict for the existing list cache
    idx_map = {orb:i for i,orb in enumerate(list_read_orbs)}
    cube_cache = CubeCache()

    # Read canonical cubes needed at R (holes+parts), but keep your return behavior
    L_1st_read = True
    orbhol, orbprt = [], []

    def _get_cmo_cube(cmo_idx, want_structure=False):
        nonlocal L_1st_read
        if cmo_idx not in idx_map or (want_structure and L_1st_read):
            cubefile = os.path.join(cmo_dir, f"{cmo_idx}.cube")
            if want_structure and (cmo_idx in idx_map):
                grid = cube_cache.read_grid(cubefile, Lnorm=True, L_structure_only=True)
                # structure-only read returns zero grid; so do a normal read right after to be safe
            natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, grid = read_cube_file(
                cubefile, Lnorm=True, L_structure_only=False
            )
            if cmo_idx not in idx_map:
                idx_map[cmo_idx] = len(list_read_orbs)
                list_read_orbs.append(cmo_idx)
                list_read_cube.append(grid)
            L_1st_read = False
            return natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, grid
        else:
            grid = list_read_cube[idx_map[cmo_idx]]
            # meta is not cached in old lists; do a cheap structure-only read only if needed
            natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, _ = read_cube_file(
                os.path.join(cmo_dir, f"{cmo_idx}.cube"), Lnorm=False, L_structure_only=True
            )
            return natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, grid

    # read holes (ensure natoms etc from first hole)
    natoms = crdorg = kabc = abc_grid = iatsrl = crdatm = None
    for i, cmo_h in enumerate(unique_holes):
        natoms, crdorg, kabc, abc_grid, iatsrl, crdatm, grid = _get_cmo_cube(cmo_h, want_structure=(i==0))
        orbhol.append(grid)

    for cmo_p in unique_parts:
        _, _, _, _, _, _, grid = _get_cmo_cube(cmo_p, want_structure=False)
        orbprt.append(grid)

    if not l_get_nhpo_cube:
        if return_svd:
            return (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm,
                    sglval, None, None,
                    list_read_orbs, list_read_cube,
                    unique_holes, unique_parts,
                    holnat, prtnat)
        else:
            return (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm,
                    sglval, None, None,
                    list_read_orbs, list_read_cube)

    na, nb, nc = orbhol[0].shape
    n_sglval = len(sglval)
    orbhol_nat, orbprt_nat = [], []

    for ihnat in range(n_sglval):
        orbsum = np.zeros((na, nb, nc), dtype=float)
        for ihcmo in range(mhorb):
            orbsum += orbhol[ihcmo] * holnat[ihcmo, ihnat]
        orbhol_nat.append(orbsum)

        orbsum = np.zeros((na, nb, nc), dtype=float)
        for ipcmo in range(nporb):
            orbsum += orbprt[ipcmo] * prtnat[ipcmo, ihnat]
        orbprt_nat.append(orbsum)

    if return_svd:
        return (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm,
                sglval, orbhol_nat, orbprt_nat,
                list_read_orbs, list_read_cube,
                unique_holes, unique_parts,
                holnat, prtnat)
    else:
        return (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm,
                sglval, orbhol_nat, orbprt_nat,
                list_read_orbs, list_read_cube)

# ============================================================
# Cross-geometry overlap blocks (your working ones kept)
# ============================================================

def build_crossgeom_cmo_overlaps(dir_R, dir_R0, occ_list, vir_list):
    cube_cache = CubeCache()
    nocc = len(occ_list)
    nvir = len(vir_list)

    S_hh = np.zeros((nocc, nocc), dtype=float)
    S_ph = np.zeros((nvir, nocc), dtype=float)

    occ_R0_grids = []
    for j in occ_list:
        occ_R0_grids.append(cube_cache.read_grid(os.path.join(dir_R0, f"{j}.cube"), Lnorm=True))

    for i, mo_i in enumerate(occ_list):
        gi = cube_cache.read_grid(os.path.join(dir_R, f"{mo_i}.cube"), Lnorm=True)
        for j, gj in enumerate(occ_R0_grids):
            S_hh[i, j] = float(np.sum(gi * gj))

    for a, mo_a in enumerate(vir_list):
        ga = cube_cache.read_grid(os.path.join(dir_R, f"{mo_a}.cube"), Lnorm=True)
        for j, gj in enumerate(occ_R0_grids):
            S_ph[a, j] = float(np.sum(ga * gj))

    return S_hh, S_ph

def compute_S_K0_for_state_NHONPO(
    unique_holes, unique_parts,
    holnat, prtnat, sglval,
    occ_list, vir_list,
    S_hh, S_ph,
    *,
    eps_norm=1e-12,
    normalize_sglval=True,
    return_debug=False,
):
    unique_holes = list(unique_holes)
    unique_parts = list(unique_parts)

    holnat = np.asarray(holnat, dtype=float)
    prtnat = np.asarray(prtnat, dtype=float)
    sglval = np.asarray(sglval, dtype=float)

    m_h = len(unique_holes)
    m_p = len(unique_parts)

    if holnat.shape != (m_h, m_h):
        raise ValueError(f"holnat shape mismatch: expected ({m_h},{m_h}), got {holnat.shape}")
    if prtnat.shape != (m_p, m_p):
        raise ValueError(f"prtnat shape mismatch: expected ({m_p},{m_p}), got {prtnat.shape}")

    n_pair = min(m_h, m_p, sglval.shape[0])
    if n_pair <= 0:
        return (0.0, {}) if return_debug else 0.0

    s = sglval[:n_pair].copy()
    if normalize_sglval:
        sn = np.linalg.norm(s)
        if sn < eps_norm:
            return (0.0, {}) if return_debug else 0.0
        s /= sn

    occ_pos = {orb: i for i, orb in enumerate(occ_list)}
    vir_pos = {orb: a for a, orb in enumerate(vir_list)}

    noccR0 = len(occ_list)
    S_hh_rows_full = np.zeros((m_h, noccR0), dtype=float)
    hole_in_window = np.array([h in occ_pos for h in unique_holes], dtype=bool)
    if not np.any(hole_in_window):
        return (0.0, {}) if return_debug else 0.0
    for L, h in enumerate(unique_holes):
        if h in occ_pos:
            S_hh_rows_full[L, :] = S_hh[occ_pos[h], :]

    S_ph_rows_full = np.zeros((m_p, noccR0), dtype=float)
    part_in_window = np.array([p in vir_pos for p in unique_parts], dtype=bool)
    if not np.any(part_in_window):
        return (0.0, {}) if return_debug else 0.0
    for M, p in enumerate(unique_parts):
        if p in vir_pos:
            S_ph_rows_full[M, :] = S_ph[vir_pos[p], :]

    V = holnat[:, :n_pair].T @ S_hh_rows_full
    W = prtnat[:, :n_pair].T @ S_ph_rows_full

    Vnorm = np.linalg.norm(V, axis=1)
    valid_K = Vnorm >= eps_norm
    if not np.any(valid_K):
        return (0.0, {}) if return_debug else 0.0

    Ctilde = np.zeros_like(V)
    Ctilde[valid_K, :] = V[valid_K, :] / Vnorm[valid_K, None]

    A = V @ Ctilde.T
    B = W @ Ctilde.T

    M = A * B
    S_K0 = float(s @ (M @ s))

    if not return_debug:
        return S_K0

    debug = dict(n_pair=n_pair, sglval_used=s.copy(), V=V, W=W, Ctilde=Ctilde,
                 valid_K=valid_K, A=A, B=B, M=M, Vnorm=Vnorm,
                 holes_in_window=hole_in_window, parts_in_window=part_in_window)
    return S_K0, debug

def compute_gs_overlap_vector(list_adiabs, ihole, ipart, cicoef, gs_cfg):
    dir_R  = gs_cfg["dir_R"]
    dir_R0 = gs_cfg["dir_R0"]
    occ_lo, occ_hi = gs_cfg["occ_range"]
    vir_lo, vir_hi = gs_cfg["vir_range"]

    occ_list = list(range(occ_lo, occ_hi + 1))
    vir_list = list(range(vir_lo, vir_hi + 1))

    #print_debug(fout,occ_list)
    #print_debug(fout,vir_list)
    S_hh, S_ph = build_crossgeom_cmo_overlaps(dir_R, dir_R0, occ_list, vir_list)
    #print_debug(fout,S_hh)
    #print_debug(fout,S_ph)

    list_read_orbs, list_read_cube = [], []
    svec = np.zeros((len(list_adiabs),), dtype=float)

    #print_debug(fout,"list_adiabats inside compute_gs_overlap_vector")
    #print_debug(fout,list_adiabs)
    for i, K in enumerate(list_adiabs):
        #print_debug(fout,i)
        #print_debug(fout,K)
        ist = K - 1
        #print_debug(fout,cicoef[ist])
        #print_debug(fout,ihole[ist])
        #print_debug(fout,ipart[ist])
        (natoms, crdorg, kabc, abc_grid, iatsrl, crdatm,
         sglval, orbhol_nat, orbprt_nat,
         list_read_orbs, list_read_cube,
         unique_holes, unique_parts,
         holnat, prtnat) = trnden_1state(
            ihole[ist], ipart[ist], cicoef[ist],
            list_read_orbs=list_read_orbs,
            list_read_cube=list_read_cube,
            l_get_nhpo_cube=False,
            return_svd=True,
            cmo_dir=gs_cfg["dir_R"]
        )
        #print_debug(fout,unique_holes)
        #print_debug(fout,unique_parts)
        #print_debug(fout,holnat)
        #print_debug(fout,prtnat)
        #print_debug(fout,sglval)
        #print_debug(fout,occ_list)
        #print_debug(fout,vir_list)
        #print_debug(fout,S_hh)
        #print_debug(fout,S_ph)

        svec[i] = compute_S_K0_for_state_NHONPO(
            unique_holes, unique_parts,
            holnat, prtnat, sglval,
            occ_list, vir_list,
            S_hh, S_ph,
            normalize_sglval=True
        )
        #print_debug(fout,svec)

    return svec

def compute_gs_gs_overlap(gs_cfg):
    dir_R  = gs_cfg["dir_R"]
    dir_R0 = gs_cfg["dir_R0"]
    occ_lo, occ_hi = gs_cfg["occ_range"]
    print_debug(fout,occ_lo)
    print_debug(fout,occ_hi)
    occ_list = list(range(occ_lo, occ_hi + 1))
    print_debug(fout,occ_list)
    S_hh, _ = build_crossgeom_cmo_overlaps(dir_R, dir_R0, occ_list, vir_list=[])
    print_debug(fout,S_hh)
    det_spatial = float(np.linalg.det(S_hh))
    print_debug(fout,det_spatial)
    return det_spatial**2

# ============================================================
# GS determinant machinery (kept, but de-duplicated with dict cache)
# ============================================================

def _is_canonical_cube_filename(path: str) -> bool:
    base = os.path.basename(path)
    return (("NHO" not in base) and ("NPO" not in base) and (re.search(r"(\d+)", base) is not None))

def _canonical_index_from_path(path: str):
    if not _is_canonical_cube_filename(path):
        return None
    m = re.search(r"(\d+)", os.path.basename(path))
    return int(m.group(1)) if m else None

def _ensure_cmo_cubes_loaded_old(mo_indices, cmo_dir, idx_list, cube_list):
    # keep your list-based cache but avoid repeated index scans by using a set
    have = set(idx_list)
    for mo in mo_indices:
        if mo in have:
            continue
        cube_path = os.path.join(cmo_dir, f"{mo}.cube")
        _, _, _, _, _, _, cube = read_cube_file(cube_path, Lnorm=True, L_structure_only=False)
        idx_list.append(mo)
        cube_list.append(cube)
        have.add(mo)

def _ensure_cmo_cubes_loaded(mo_indices, cmo_dir, idx_list, cube_list):
    have = set(idx_list)
    for mo in mo_indices:
        if mo in have:
            continue
        cube_path = os.path.join(cmo_dir, f"{mo}.cube")
        _, _, _, _, _, _, cube = read_cube_file(cube_path, Lnorm=True, L_structure_only=False)
        idx_list.append(mo)
        cube_list.append(cube)
        have.add(mo)


def build_Soo_Sov_from_cubes(gs_cfg, cache_paths_R0, cache_cubes_R0, list_read_cmo_idx, list_read_cmo_cube):
    dir_R0 = gs_cfg["dir_R0_cmo"]
    occ_R  = gs_cfg["occ_R"]
    occ_R0 = gs_cfg["occ_R0"]
    vir_R0 = gs_cfg["vir_R0"]

    noccR  = len(occ_R)
    noccR0 = len(occ_R0)
    nvirR0 = len(vir_R0)

    posR = {orb:i for i,orb in enumerate(list_read_cmo_idx)}
    for orbR in occ_R:
        if orbR not in posR:
            raise ValueError(f"occ_R orbital {orbR} missing in list_read_cmo_idx")

    # cache R0 cubes via path lists to preserve your behavior
    def _read_cached_R0(path):
        ap = os.path.abspath(path)
        if ap in cache_paths_R0:
            return cache_cubes_R0[cache_paths_R0.index(ap)]
        _, _, _, _, _, _, cube = read_cube_file(ap, Lnorm=True, L_structure_only=False)
        cache_paths_R0.append(ap)
        cache_cubes_R0.append(cube)
        return cube

    occ_R0_cubes = [ _read_cached_R0(os.path.join(dir_R0, f"{q}.cube")) for q in occ_R0 ]
    vir_R0_cubes = [ _read_cached_R0(os.path.join(dir_R0, f"{a}.cube")) for a in vir_R0 ]

    S_oo = np.zeros((noccR, noccR0), dtype=float)
    S_ov = np.zeros((noccR, nvirR0), dtype=float)

    for p, orbR in enumerate(occ_R):
        cube_R = list_read_cmo_cube[posR[orbR]]
        for q in range(noccR0):
            S_oo[p, q] = float(np.sum(cube_R * occ_R0_cubes[q]))
        for a in range(nvirR0):
            S_ov[p, a] = float(np.sum(cube_R * vir_R0_cubes[a]))

    return S_oo, S_ov

def det_column_replaced(S_oo, col_q, new_col_vec):
    M = np.array(S_oo, copy=True)
    M[:, col_q] = new_col_vec
    return float(np.linalg.det(M))

def _project_target_cube_onto_basis_R0(target_cube_R0, basis_indices_R0, dir_R0_cmo, cache_paths_R0, cache_cubes_R0):
    s = np.zeros((len(basis_indices_R0),), dtype=float)

    for j, idx in enumerate(basis_indices_R0):
        ap = os.path.abspath(os.path.join(dir_R0_cmo, f"{idx}.cube"))
        if ap in cache_paths_R0:
            cube_j = cache_cubes_R0[cache_paths_R0.index(ap)]
        else:
            _, _, _, _, _, _, cube_j = read_cube_file(ap, Lnorm=True, L_structure_only=False)
            cache_paths_R0.append(ap)
            cache_cubes_R0.append(cube_j)
        s[j] = float(np.sum(cube_j * target_cube_R0))

    nrm = np.linalg.norm(s)
    if nrm < 1e-14:
        raise ValueError("Projection onto R0 basis is ~0")
    return s / nrm

def compute_overlap_GS_R_with_ref_CIstate_R0(ref_state, gs_cfg, S_oo, S_ov, cache_paths_R0, cache_cubes_R0):
    dir_R0_cmo = gs_cfg["dir_R0_cmo"]
    occ_R0 = gs_cfg["occ_R0"]
    vir_R0 = gs_cfg["vir_R0"]

    # cache projected coeff vectors per file
    hole_coeff_map = {}
    part_coeff_map = {}
    cube_cache_local = CubeCache()

    for holecube_file, partcube_file, _ in ref_state:
        hole_idx = _canonical_index_from_path(holecube_file)
        part_idx = _canonical_index_from_path(partcube_file)

        if hole_idx is None and holecube_file not in hole_coeff_map:
            hole_cube = cube_cache_local.read_grid(holecube_file, Lnorm=True)
            hole_coeff_map[holecube_file] = _project_target_cube_onto_basis_R0(
                hole_cube, occ_R0, dir_R0_cmo, cache_paths_R0, cache_cubes_R0
            )

        if part_idx is None and partcube_file not in part_coeff_map:
            part_cube = cube_cache_local.read_grid(partcube_file, Lnorm=True)
            part_coeff_map[partcube_file] = _project_target_cube_onto_basis_R0(
                part_cube, vir_R0, dir_R0_cmo, cache_paths_R0, cache_cubes_R0
            )

    # optional MGS in coefficient space (your option)
    if bool(gs_cfg.get("orthogonalize_tildeh", False)):
        if len(hole_coeff_map) >= 2:
            keys = list(hole_coeff_map.keys())
            C = np.column_stack([hole_coeff_map[k] for k in keys])
            Q = mgs_orthonormalize_columns(C)
            for j, k in enumerate(keys):
                hole_coeff_map[k] = Q[:, j]
        if len(part_coeff_map) >= 2:
            keys = list(part_coeff_map.keys())
            C = np.column_stack([part_coeff_map[k] for k in keys])
            Q = mgs_orthonormalize_columns(C)
            for j, k in enumerate(keys):
                part_coeff_map[k] = Q[:, j]

    ovlp = 0.0
    for holecube_file, partcube_file, c in ref_state:
        c = float(c)
        hole_idx = _canonical_index_from_path(holecube_file)
        part_idx = _canonical_index_from_path(partcube_file)

        # choose replaced column
        if hole_idx is not None:
            col_q = occ_R0.index(hole_idx)
        else:
            c_occ = hole_coeff_map[holecube_file]
            col_q = int(np.argmax(np.abs(c_occ)))

        # build replacement column
        if part_idx is not None:
            aind = vir_R0.index(part_idx)
            new_col = S_ov[:, aind]
        else:
            c_vir = part_coeff_map[partcube_file]
            new_col = S_ov @ c_vir

        ovlp += c * det_column_replaced(S_oo, col_q, new_col)

    return float(ovlp)

# ============================================================
# DIABATIZATION (Strategy A) — kept physically identical, optimized caching
# ============================================================

def diabatize_states_EKa(
    list_adiabs, list_ref_states, cp2k_output, Eref=0.0, small=0.1,
    list_group_diabs_start_ind=None, list_group_diabs_properties=None,
    lwrite=False, gs_cfg=None
):
    """
    This keeps Strategy A logic (including GS group) identical,
    but replaces slow list.index caches with dict caches.
    """
    global fout  # Required to modify the global variable
    fout=open("debug_output","w")
    fout.write(f"\nThis is a debug printing file to understand code mechanism\n")

    if list_group_diabs_start_ind is None: list_group_diabs_start_ind = []
    if list_group_diabs_properties is None: list_group_diabs_properties = []

    ihole, ipart, cicoef, osc_list, Eorb, Estate, E_scf = read_cp2k_output(cp2k_output, small)
    print(f"E_scf = {E_scf} Hartree")
    #print_debug(fout,gs_enable)

    gs_enable = bool(gs_cfg) and gs_cfg.get("enable", False)
    print_debug(fout,gs_enable)

    n_adiab_exc = len(list_adiabs)
    EXC_OFFSET  = 1 if gs_enable else 0
    n_adiab_ext = n_adiab_exc + EXC_OFFSET
    GS_ADIAB_INDEX = 0 if gs_enable else None

    n_diab_base = len(list_ref_states)
    n_diab = n_diab_base + (1 if gs_enable else 0)

    Rotmat_adiab_diab = np.zeros((n_adiab_ext, n_diab), dtype=float)

    # --- read adiabatic states, build CMO cache at R
    # --- Build the CMO cube cache at R without doing any SVD (no trnden_1state here)
    list_read_cmo_idx, list_read_cmo_cube = [], []

    cmo_dir = gs_cfg["dir_R"] if (gs_cfg and "dir_R" in gs_cfg) else "."

    needed_cmos = _collect_needed_cmos(list_adiabs, ihole, ipart)
    _ensure_cmo_cubes_loaded(needed_cmos, cmo_dir, list_read_cmo_idx, list_read_cmo_cube)

    # Energies for the selected adiabats (excited-only list)
    Estate_in_adiab_list = [Estate[K - 1] for K in list_adiabs]

    # fast lookup: CMO index -> position in list_read_cmo_cube
    cmo_pos = {orb: i for i, orb in enumerate(list_read_cmo_idx)}
    print_debug(fout,cmo_pos)

    # --- adiab-adiab overlap check (excited-only; identical math)
    n_adiab = n_adiab_exc
    S_adiab_adiab = np.zeros((n_adiab, n_adiab), dtype=float)
    for i in range(n_adiab):
        istate = list_adiabs[i] - 1
        amps_i = cicoef[istate]; holes_i = ihole[istate]; parts_i = ipart[istate]
        for j in range(i, n_adiab):
            jstate = list_adiabs[j] - 1
            amps_j = cicoef[jstate]; holes_j = ihole[jstate]; parts_j = ipart[jstate]
            ov = 0.0
            for ai, hi, pi in zip(amps_i, holes_i, parts_i):
                for aj, hj, pj in zip(amps_j, holes_j, parts_j):
                    if hi == hj and pi == pj:
                        ov += ai * aj
            S_adiab_adiab[i, j] = ov
            S_adiab_adiab[j, i] = ov

    print("\nOverlap matrix between adiabats")
    print_matrix(S_adiab_adiab)
    print(f"Determinant of the matrix: {np.linalg.det(S_adiab_adiab)}")

    accumulated_prjmat = np.zeros((n_adiab_ext, n_adiab_ext), dtype=float)
    list_prjmat = []

    # --- GS precompute (same as your working code)
    if gs_enable:
        required = ["dir_R0", "dir_R", "occ_R", "occ_R0", "vir_R0", "occ_range", "vir_range", "dir_R0_cmo"]
        missing = [k for k in required if k not in gs_cfg]
        if missing:
            raise KeyError(f"[GS] Missing gs_cfg keys: {missing}")

        if "cache_paths_R0" not in gs_cfg:
            gs_cfg["cache_paths_R0"] = []
            gs_cfg["cache_cubes_R0"] = []
        cache_paths_R0 = gs_cfg["cache_paths_R0"]
        cache_cubes_R0 = gs_cfg["cache_cubes_R0"]

        _ensure_cmo_cubes_loaded(gs_cfg["occ_R"], gs_cfg["dir_R"], list_read_cmo_idx, list_read_cmo_cube)
        # rebuild map because we appended
        cmo_pos = {orb:i for i,orb in enumerate(list_read_cmo_idx)}

        if ("S_oo" not in gs_cfg) or ("S_ov" not in gs_cfg):
            S_oo, S_ov = build_Soo_Sov_from_cubes(gs_cfg, cache_paths_R0, cache_cubes_R0, list_read_cmo_idx, list_read_cmo_cube)
            gs_cfg["S_oo"] = S_oo
            gs_cfg["S_ov"] = S_ov
        else:
            S_oo = gs_cfg["S_oo"]
            S_ov = gs_cfg["S_ov"]

    # --- groups: GS + excited groups
    if gs_enable:
        groups = [("GS", None)] + [("EXC", g) for g in list_ref_states]
    else:
        groups = [("EXC", g) for g in list_ref_states]

    # reference cube cache (R0 NHO/NPO cubes) + overlap caches
    ref_cube_cache = CubeCache()
    # overlap cache: (ref_abs_path, cmo_index) -> float
    ovlp_cache = {}

    for igroup, (gkind, ref_group) in enumerate(groups):
        col = igroup #col for diabats, row for adiabats
        print(f"\nLooping igroup={igroup}, gkind={gkind}")

        if gkind == "GS":
            print("\n[GS-GROUP] Building GS projector")
            svec_exc = compute_gs_overlap_vector(list_adiabs, ihole, ipart, cicoef, gs_cfg)
            print_debug(fout,svec_exc)
            s00 = compute_gs_gs_overlap(gs_cfg)
            print_debug(fout,s00)
            print(f"s00 = {s00}")

            S_ext = np.zeros((n_adiab_ext, 1), dtype=float)
            #print_debug(fout,S_ext)
            S_ext[GS_ADIAB_INDEX, 0] = s00
            #print_debug(fout,GS_ADIAB_INDEX)
            #print_debug(fout,S_ext)
            S_ext[EXC_OFFSET:, 0] = svec_exc
            #print_debug(fout,EXC_OFFSET)
            print_debug(fout,S_ext)
            #print_debug(fout,S_ext.T)

            prjmat_use = S_ext @ S_ext.T
            #print_debug(fout,prjmat_use)
            #print_debug(fout,accumulated_prjmat)
            accumulated_prjmat += prjmat_use
            #print_debug(fout,accumulated_prjmat)
            #print_debug(fout,list_prjmat)

            list_prjmat.append(prjmat_use)
            #print_debug(fout,list_prjmat)

            # Strategy A in your code: eigenvector of rank-1 projector aligned with S_ext
            w, v = np.linalg.eigh(prjmat_use)
            print(f'\nThe eigenvectors with the two largest eigenvalues of prjmat\n')
            print_eigen_solution(w[-2:], v[:,-2:])
            ref_vec = S_ext[:, 0]
            phase = np.sign(np.sum(v[:, -1] * ref_vec)) or 1.0
            Rotmat_adiab_diab[:, col] = v[:, -1] * phase
            print_debug(fout,"First, GS column")
            print_debug(fout,Rotmat_adiab_diab)
            continue

        # EXC group
        n_refstates = len(ref_group)
        S_adiab_refstate = np.zeros((n_adiab_exc, n_refstates), dtype=float)

        for iref_state, ref_state in enumerate(ref_group):
            n_holprt = len(ref_state)
            c_array = np.array([hp[2] for hp in ref_state], dtype=float)
            dnorm = np.linalg.norm(c_array)
            if dnorm < 1e-14:
                raise ValueError(f"Reference state {iref_state} has zero norm")
            c_array /= dnorm

            for iholprt, holprt in enumerate(ref_state):
                holecube_file, partcube_file = holprt[0], holprt[1]
                ref_hole_cube = ref_cube_cache.read_grid(holecube_file, Lnorm=True)
                ref_part_cube = ref_cube_cache.read_grid(partcube_file, Lnorm=True)
                cref = c_array[iholprt]

                for iadiab, K in enumerate(list_adiabs):
                    istate = K - 1
                    amps = cicoef[istate]
                    holes = ihole[istate]
                    parts = ipart[istate]
                    #print_debug(fout,amps)
                    #print_debug(fout,holes)
                    #print_debug(fout,parts)

                    S_adiab_refhp = 0.0
                    for amp, h_orb, p_orb in zip(amps, holes, parts):
                        h_cube = list_read_cmo_cube[cmo_pos[h_orb]]
                        p_cube = list_read_cmo_cube[cmo_pos[p_orb]]

                        key_h = (os.path.abspath(holecube_file), h_orb)
                        key_p = (os.path.abspath(partcube_file), p_orb)

                        if key_h in ovlp_cache:
                            hole_ov = ovlp_cache[key_h]
                        else:
                            hole_ov = float(np.sum(ref_hole_cube * h_cube))
                            ovlp_cache[key_h] = hole_ov

                        if key_p in ovlp_cache:
                            part_ov = ovlp_cache[key_p]
                        else:
                            part_ov = float(np.sum(ref_part_cube * p_cube))
                            ovlp_cache[key_p] = part_ov

                        S_adiab_refhp += amp * hole_ov * part_ov

                    S_adiab_refstate[iadiab, iref_state] += S_adiab_refhp * cref

        print("\nOverlap matrix between adiabats and reference states (excited-only)")
        print_matrix(S_adiab_refstate)

        if gs_enable:
            S_ext = np.zeros((n_adiab_ext, n_refstates), dtype=float)
            print_debug(fout,S_ext)
            S_ext[EXC_OFFSET:, :] = S_adiab_refstate
            print_debug(fout,S_ext)

            for jref, ref_state in enumerate(ref_group):
                fout.write(f"\nS_ext[GS_ADIAB_INDEX, jref]  {GS_ADIAB_INDEX}_{jref}\n")
                S_ext[GS_ADIAB_INDEX, jref] = compute_overlap_GS_R_with_ref_CIstate_R0(
                    ref_state, gs_cfg, S_oo, S_ov, cache_paths_R0, cache_cubes_R0
                )
            print_debug(fout,S_ext)

            prjmat_use = S_ext @ S_ext.T
            ref_vec = S_ext[:, 0]
        else:
            prjmat_use = S_adiab_refstate @ S_adiab_refstate.T
            ref_vec = S_adiab_refstate[:, 0]

        accumulated_prjmat += prjmat_use
        list_prjmat.append(prjmat_use)
        #print_debug(fout,prjmat_use)
       
        w, v = np.linalg.eigh(prjmat_use)
        print(f'\nThe eigenvectors with the two largest eigenvalues of prjmat\n')
        print_eigen_solution(w[-2:], v[:,-2:])

        fout.write(f"\nRotmat_adiab_diab for GS + {gkind}_{igroup}\n")
        #print_debug(fout,w)
        #print_debug(fout,v)
        phase = np.sign(np.sum(v[:, -1] * ref_vec)) or 1.0
        Rotmat_adiab_diab[:, col] = v[:, -1] * phase

        #fout.write(f"\nRotmat_adiab_diab for GS + {gkind}_{igroup}\n")
        #print_debug(fout,Rotmat_adiab_diab)


    print("\nRotmat_adiab_diab from Strategy A (includes GS group if enabled)")
    print_matrix(Rotmat_adiab_diab)

    # ----- reduced space (kept from your original behavior)
    acumprj_eigval, acumprj_eigvec = np.linalg.eigh(accumulated_prjmat)
    n_keep = n_diab
    cut = n_adiab_ext - n_keep

    projval_in_alldiabs = np.sum(acumprj_eigval[cut:])
    leftover_prjval     = np.sum(acumprj_eigval[:cut])
    print(f"\nTotal projection length^2 of all adiabs in all diabs: {projval_in_alldiabs}")
    print(f"\nLeftover length^2 of all adiabs out of all diabs: {leftover_prjval}")

    reduced_adiabs_space = acumprj_eigvec[:, cut:]
    print(f'\nDimensions of reduced_adiabs_space: {reduced_adiabs_space.shape}')

    # energies in extended space
    EH2EV = 27.211386245981
    Estate_Hartree = Estate / EH2EV + E_scf

    if gs_enable:
        Estate_ext = np.zeros(n_adiab_ext, dtype=float)
        Estate_ext[EXC_OFFSET:] = np.array(Estate_in_adiab_list, dtype=float)
        Eadiab_diag_mat = np.diag(Estate_ext)
    else:
        Eadiab_diag_mat = np.diag(np.array(Estate_in_adiab_list, dtype=float))

    print(f'\nEadiab_diag_mat, which is in eV unit and ground state E is 0 eV:\n')
    print_matrix(Eadiab_diag_mat)

    Hmat_reduced_space = reduced_adiabs_space.T @ Eadiab_diag_mat @ reduced_adiabs_space
    Estate_reduced_adiab, eigvec = np.linalg.eigh(Hmat_reduced_space)
    reduced_adiabs_space = reduced_adiabs_space @ eigvec
    print(f'\nEstate_reduced_adiab:\n')
    print(Estate_reduced_adiab)

    Rotmat_reduced_adiab_diab = np.zeros((n_adiab_ext, n_diab), dtype=float)
    for icol, prjmat in enumerate(list_prjmat):
        reduced_prjmat = reduced_adiabs_space.T @ prjmat @ reduced_adiabs_space
        prj_eigval, prj_eigvec = np.linalg.eigh(reduced_prjmat)
        Rotmat_reduced_adiab_diab[:, icol] = reduced_adiabs_space @ prj_eigvec[:, -1]
        phase = np.sign(np.dot(Rotmat_reduced_adiab_diab[:, icol], Rotmat_adiab_diab[:, icol])) or 1.0
        Rotmat_reduced_adiab_diab[:, icol] *= phase

    # ----- symmetric orthogonalization (same as your code)
    print("\nRotational matrix before symmetric orthogonalization:")
    print_matrix(Rotmat_adiab_diab)
    S = Rotmat_adiab_diab.conj().T @ Rotmat_adiab_diab
    print("Overlap matrix of the diabatic states")
    print_matrix(S)
    sym_ortho = symmetric_orthogonalization(S)
    Rotmat_adiab_diab = Rotmat_adiab_diab @ sym_ortho
    print("\nRotational matrix after symmetric orthogonalization:")
    print_matrix(Rotmat_adiab_diab)

    # --- Check orthonormality of col vectors in Rotmat_reduced_adiab_diab
    S = Rotmat_reduced_adiab_diab.T @  Rotmat_reduced_adiab_diab
    print("Overlap matrix of the diabatic states in the reducd adiab space")
    print_matrix(S)
    sym_ortho = symmetric_orthogonalization(S)
    Rotmat_reduced_adiab_diab = Rotmat_reduced_adiab_diab @ sym_ortho
    print("\nRotational matrix in reduced adiab space after symmetric orthogonalization:")
    print_matrix(Rotmat_reduced_adiab_diab)

    # ----- build H(adiab) and H(diab) exactly like before
   #Hmat_adiab = np.zeros((n_adiab_ext, n_adiab_ext), dtype=float)
    Hmat_adiab =  Eadiab_diag_mat / EH2EV + (E_scf  - Eref)*np.eyes(Eadiab_diag_mat.shape[0])
   #if gs_enable:
   #    Hmat_adiab[GS_ADIAB_INDEX, GS_ADIAB_INDEX] = (E_scf - Eref)
   #for ii, state in enumerate(list_adiabs):
   #    istate = state - 1
   #    if gs_enable:
   #        Hmat_adiab[ii + EXC_OFFSET, ii + EXC_OFFSET] = (Estate_Hartree[istate] - Eref)
   #    else:
   #        Hmat_adiab[ii, ii] = (Estate_Hartree[istate] - Eref)

    Hmat_diab_hartree = Rotmat_adiab_diab.conj().T @ Hmat_adiab @ Rotmat_adiab_diab

    # ----- legacy prints (your exact format)
    print(f"\nHamiltonian matrix of adiabats in hartree, with Eref = {Eref} hartree:")
    print_matrix(Hmat_adiab)

    print(f"\nHamiltonian matrix of diabats in hartree, with Eref = {Eref} hartree:")
    print_matrix(Hmat_diab_hartree)

    print(f"\nAdiabatic energies, with Eref = {Eref} hartree:")
    for i in range(n_adiab_ext):
        print("Adiabat %3d: %15.8f Hartree, %15.8f eV" % (i, Hmat_adiab[i, i], Hmat_adiab[i, i] * EH2EV))

    print(f"\nDiagonal Hamiltonian matrix elements of diabats, with Eref = {Eref} hartree:")
    for i in range(n_diab):
        print("Diabat %3d: %15.8f Hartree, %15.8f eV" % (i, Hmat_diab_hartree[i, i], Hmat_diab_hartree[i, i] * EH2EV))

    print("\nOff-diagonal Hamiltonian matrix elements of diabats:")
    for i in range(n_diab):
        for j in range(i + 1, n_diab):
            print("Diabat pair %3d, %3d: %15.8f Hartree, %15.8f eV" %
                  (i, j, Hmat_diab_hartree[i, j], Hmat_diab_hartree[i, j] * EH2EV))

    if n_adiab_ext > n_diab:
        print(f'Dimensions of Rotmat_reduced_adiab_diab: {Rotmat_reduced_adiab_diab.shape}')
        print(f'Dimension of Estate_reduced_adiab: {len(Estate_reduced_adiab),Estate_reduced_adiab}')
        Hmat_diab_reduced_adiab = Rotmat_reduced_adiab_diab.T @ Hmat_adiab @ Rotmat_reduced_adiab_diab
        print(f"\nDiagonal Hamiltonian matrix elements of diabats in reduced adiab space, with Eref = {Eref} hartree:")
        for i in range(n_diab):
            print("Diabat %3d: %15.8f Hartree, %15.8f eV" % (i, Hmat_diab_reduced_adiab[i, i], Hmat_diab_reduced_adiab[i, i] * EH2EV))

        print("\nOff-diagonal Hamiltonian matrix elements of diabats in reduced adiab space:")
        for i in range(n_diab):
            for j in range(i + 1, n_diab):
                print("Diabat pair %3d, %3d: %15.8f Hartree, %15.8f eV" %
                      (i, j, Hmat_diab_reduced_adiab[i, j], Hmat_diab_reduced_adiab[i, j] * EH2EV))

    fout.close()

    return Rotmat_adiab_diab, Hmat_diab_hartree

