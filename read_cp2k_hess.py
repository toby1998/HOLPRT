import sys
from utils_holprt import *

cp2k_hess_molden = sys.argv[1]
cp2k_hess_input = sys.argv[2]

atom_xyzcrd_bohr,atom_frccrd,abc_vec,b_vec,freq_list,modes_disp,mass_amu_list,atom_list = read_cp2k_hess_output(cp2k_hess_molden,cp2k_hess_input)

phonon_dos(freq_list)

ncells = [4,4,1]
kmesh_info = get_k_info(ncells)
atom_cell_ind,atom_corspnd_0cell,abc_unitcell_vec,b_unitcell_vec = getK_modes(atom_xyzcrd_bohr,atom_frccrd,abc_vec,b_vec,freq_list,modes_disp,ncells,mass_amu_list,kmesh_info)
purifyK_modes(atom_cell_ind,atom_corspnd_0cell,abc_unitcell_vec,b_unitcell_vec,freq_list,modes_disp,ncells,mass_amu_list,kmesh_info,atom_xyzcrd_bohr,atom_list)
