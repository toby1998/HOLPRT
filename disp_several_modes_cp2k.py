import sys
from utils_holprt import *

cp2k_hess_molden = sys.argv[1]
qdisp = float(sys.argv[2])

atom_xyzcrd_bohr,freq_list,modes_disp,mass_amu_list,atom_list = read_molden_hessian(cp2k_hess_molden)

for freq in freq_list:
    mode_disp(atom_xyzcrd_bohr,freq_list,modes_disp,mass_amu_list,atom_list,freq,qdisp)
