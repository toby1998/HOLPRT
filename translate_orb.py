import sys
from utils_holprt import *

cubefile = 'VBM_G_layer1_sym.cube'

vec_translate= np.array([0.0,0.0,9.5142035])

natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube = read_cube_file(cubefile)

translate_orbcube(natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube,vec_translate,Lwrite = True)
