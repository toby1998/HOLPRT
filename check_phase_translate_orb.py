import sys
from utils_holprt import *

"""
Check the phase consistence of a set of orbitals. The first orbital in the set is the reference. It is shifted to the layers of the other orbitals.
The overlap between the shifted orbital and the orbital at that layer is calculated.
If the overlap is negative, flip the phase of the orbital at that layer.
"""

list_cube_files = []
for layer in range(1,7):
    filnam = 'VBM_G_layer'+str(layer)+'_sym.cube'
   #filnam = 'VBM_G_layer'+str(layer)+'_antisym.cube'
   #filnam = 'CBM_G_layer'+str(layer)+'_0.cube'
   #filnam = 'CBM_M_layer'+str(layer)+'_kmesh220.cube'
    list_cube_files.append(filnam)

# zlayer for SiH(1H)
#zlayer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
# zlayer for SiH(1H) 6 layers + vacuum
zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]

assert len(list_cube_files) == len(zlayer)

natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer1 = read_cube_file(list_cube_files[0])
#norm_cube_layer1 = np.sum(cube_layer1*cube_layer1)
#print(f'norm_cube_layer1: {norm_cube_layer1}')

for layer in range(2,7):
    z_shift = zlayer[layer-1] - zlayer[0]
    vec_translate = np.array([0.0,0.0,z_shift])
    print(layer,vec_translate)
    shifted_cube = translate_orbcube(natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer1,vec_translate,Lwrite=False)
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer_i = read_cube_file(list_cube_files[layer-1])
   #norm_cube = np.sum(cube_layer_i*cube_layer_i)
   #print(f'norm_cube_layer{layer}: {norm_cube}')
    ovrlap = np.sum(shifted_cube*cube_layer_i)
    print(f'Layer {layer}: ovrlap: {ovrlap}')
    if ovrlap < 0.0:
        print(f'Flippint phase for {list_cube_files[layer-1]}')
        cube_layer_i *= -1.0
        filnam = list_cube_files[layer-1]
        write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_layer_i,'\n')

#vec_translate= np.array([0.0,0.0,9.5142035])

#natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube = read_cube_file(cubefile)

#translate_orbcube(natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,read_in_cube,vec_translate,Lwrite = True)
