import sys
from utils_holprt import *

"""
Check the phase consistence of a set of orbitals. The first orbital in the set is the reference. It is shifted to the layers of the other orbitals.
The overlap between the shifted orbital and the orbital at that layer is calculated.
If the overlap is negative, flip the phase of the orbital at that layer.
"""

#cubefile_layer1 = 'CBM_G_layer1.cube'
#cubefile_layer1 = 'VBM_G_layer1_antisym_220.cube'
cubefile_layer1 = 'VBM_G_layer1_antisym_020.cube'


# zlayer for SiH(1H)
#zlayer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
# zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#zlayer for SiH(3R)
#zlayer = [4.68978,14.0690585,23.448337,32.8278965,42.207175,51.586453]
#zlayer for SiH(3R) 6 layers + vacuum
#zlayer = [4.689897,14.0687508,23.448545,32.8278692,42.207193,51.586517]
# zlayer for SiH(6R)
#zlayer = [9.4622680,18.9248200,28.3870880,37.8493560,47.3119080,56.77417385555148]
# zlayer for SiH(6R) 6 layers vac
zlayer = [4.344959,13.807503,23.270047,32.732591,42.195135,51.657206]

#assert len(list_cube_files) == len(zlayer)

natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer1 = read_cube_file(cubefile_layer1)
#norm_cube_layer1 = np.sum(cube_layer1*cube_layer1)
#print(f'norm_cube_layer1: {norm_cube_layer1}')

for layer in range(2,7):
    z_shift = zlayer[layer-1] - zlayer[0]
    vec_translate = np.array([0.0,0.0,z_shift])
    print(layer,vec_translate)
    shifted_cube = translate_orbcube(natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer1,vec_translate,Lwrite=False)

    list_orb_proj_to = ['Shifted_cube']
    cube_orb_proj_to = [shifted_cube]

    list_orb_to_proj = []
   #for iorb in range(3):
   #    filnam = 'CBM_M_layer' + str(layer) + '_' + str(iorb) + '.cube'
   #    list_orb_to_proj.append(filnam)
    for iorb in range(2):
        filnam = 'VBM_G_layer' + str(layer) + '_' + str(iorb) + '.cube'
        list_orb_to_proj.append(filnam)
   #filnam = 'CBM_M_layer' + str(layer) + '_kmesh020.cube'
   #list_orb_to_proj = [filnam]

    cube_orb_to_proj=[]

    n_collect = 1
    list_proj_cube = proj_orbs(list_orb_to_proj,list_orb_proj_to,n_collect,cube_orb_to_proj,cube_orb_proj_to,lwrite=False)

   #filnam = 'CBM_M_layer' + str(layer) + '_kmesh020.cube'
    filnam = 'VBM_G_layer' + str(layer) + '_antisym_020.cube'
   #filnam = 'CBM_G_layer' + str(layer) + '.cube'

    write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_proj_cube[0],'\n')

#vec_translate= np.array([0.0,0.0,9.5142035])

#natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube = read_cube_file(cubefile)

#translate_orbcube(natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube,vec_translate,Lwrite = True)
