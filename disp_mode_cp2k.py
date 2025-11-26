import sys
from utils_holprt import *

cp2k_hess_molden = sys.argv[1]
freq_mode_disp = float(sys.argv[2])
qdisp = float(sys.argv[3])

atom_xyzcrd_bohr,freq_list,modes_disp,mass_amu_list,atom_list = read_molden_hessian(cp2k_hess_molden)

#qdisp = 0.05 #qdisp read from input
mode_disp(atom_xyzcrd_bohr,freq_list,modes_disp,mass_amu_list,atom_list,freq_mode_disp,qdisp)
