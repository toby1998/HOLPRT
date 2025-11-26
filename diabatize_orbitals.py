import sys
from utils_holprt import *


list_canon_orb = [79,80,81,82,83,84]
#list_reforb_cube is a list of list. Each sub-list has cube files of a group of reference orbitals to give one diabatic orbital
list_reforb_cube = [['../VBMG_sym_longaxis_with_CBMM220.cube'],['../VBMG_antisym_longaxis_with_CBMM220.cube'],['../CBM_G.cube'],['../CBM_M_kmesh200.cube'],['../CBM_M_kmesh020.cube'],['../CBM_M_kmesh220.cube']]
#list_reforb_cube = [['./VBMG_sym_longaxis_with_CBMM220.cube'],['./VBMG_antisym_longaxis_with_CBMM220.cube'],['./CBM_G.cube'],['./CBM_M_kmesh200.cube'],['./CBM_M_kmesh020.cube'],['./CBM_M_kmesh220.cube']]

lwrite = True
cp2k_output = 'SiH_4X4X1.out'


diabatize_orbitals(list_canon_orb,list_reforb_cube,cp2k_output,lwrite)
