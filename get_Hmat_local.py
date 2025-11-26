import sys
from utils_holprt import *



#Test of getting local orbitals' energies Start
outfile = 'GeH_4X4X2.out'
#outfile = 'SiH_3R_442.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile)
canon_list = []
#for iorb in range(469,480+1):
for iorb in range(481,486+1):
   canon_list.append(iorb)
#canon_list = [484,485,486,487,488,489]
#CBM_G(ML) orbitals in SiH(1H)
#canon_list = [481,482,483,502,503,504]
#CBM_G(ML) orbitals in SiH(1H) 6layers vac
#canon_list = [481,482,492,499,503,504]
#remove = [481,482,492,499,503,504]
#CBM_G(ML) orbitals in SiH(3R) 6 layers vac
#canon_remove = [485,488,489,493,494,495]
#CBM_G(ML) orbitals in SiH(3R)
#canon_remove = [484,489,491,493,494,495]
#CBM_G(ML) orbitals in SiH(6R)
#canon_list = [481,482,483,502,503,504]
#CBM_G(ML) orbitals in SiH(6R) 6layers vac
#canon_remove = [481,482,492,502,503,504]
#canon_list = list(set(canon_list) - set(canon_remove))

#locorb_cubefile_list = ['VBM_G_layer1_0.cube','VBM_G_layer1_1.cube','VBM_G_layer2_0.cube','VBM_G_layer2_1.cube','VBM_G_layer3_0.cube','VBM_G_layer3_1.cube','VBM_G_layer4_0.cube','VBM_G_layer4_1.cube','VBM_G_layer5_0.cube','VBM_G_layer5_1.cube','VBM_G_layer6_0.cube','VBM_G_layer6_1.cube']
#locorb_cubefile_list = ['CBM_G_layer1_0.cube','CBM_G_layer2_0.cube','CBM_G_layer3_0.cube','CBM_G_layer4_0.cube','CBM_G_layer5_0.cube','CBM_G_layer6_0.cube']
#locorb_cubefile_list = ['VBMG_sym_longaxis_with_CBMM220.cube','VBMG_antisym_longaxis_with_CBMM220.cube','CBM_G.cube','CBM_M_kmesh200.cube','CBM_M_kmesh020.cube','CBM_M_kmesh220.cube']
#locorb_cubefile = 'State10_Layer1_prjprt0.cube'
#locorb_cubefile_list.append(locorb_cubefile)
locorb_cubefile_list = []
for layer in range(1,6+1):
   #filnam = 'CBM_M_layer' + str(layer) + '_kmesh220.cube'
    filnam = 'CBM_G_layer' + str(layer) + '.cube'
   #filnam = 'VBM_G_layer' + str(layer) + '_antisym_020.cube'
   #filnam = 'VBM_G_layer' + str(layer) + '_0.cube'
    locorb_cubefile_list.append(filnam)
   #filnam = 'VBM_G_layer' + str(layer) + '_antisym_220.cube'
   #filnam = 'VBM_G_layer' + str(layer) + '_1.cube'
   #locorb_cubefile_list.append(filnam)

L_rot_locorb = False
glocorb = 3
nlayer = 6
locorb_interest = 0
Hmat_locorb, locorb_cube_list = get_Hmat_locorb(canon_list,locorb_cubefile_list,Eorb,L_rot_locorb,glocorb,nlayer,locorb_interest)

#if L_rot_locorb: degen_locorb_rot_H(Hmat_locorb,locorb_cube_list,glocorb,nlayer,locorb_interest,Lpbc)

#Test of getting local orbitals' energies End
