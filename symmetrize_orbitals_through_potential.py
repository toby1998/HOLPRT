import sys
from utils_holprt import *
import numpy as np

##Test of localizing orbitals start

#orb_list = []
#for iorb in range(469,481):
#    orb_list.append(iorb)
#orb_list = [481,482,483,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504]
#orb_list = [481,482,483,502,503,504]



list_cube_files = ['VBM_G_layer3_0.cube','VBM_G_layer3_1.cube']
orb_cube_list = []
for cubefile in list_cube_files:
    file_exists(cubefile)
    print(f'Reading {cubefile}')
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(cubefile,True)
    orb_cube_list.append(cube_grid)

[na,nb,nc] = orb_cube_list[0].shape
print(na,nb,nc)
gaus_center_1 = np.array([0.0,0.0])
gaus_center_2 = na*abc_grid[0,0:2]+nb*abc_grid[1,0:2]
gauss_scale = 10e7
print(gaus_center_1,gaus_center_2)
#set potential for one layer
vpot = np.zeros([na,nb])
sigma = 0.002
for ia in range(kabc[0]):
    for ib in range(kabc[1]):
        r = ia*abc_grid[0,0:2]+ib*abc_grid[1,0:2]
        r1 = r - gaus_center_1
        dist1 = np.linalg.norm(r1)
        r2 = r - gaus_center_2
        dist2 = np.linalg.norm(r2)
        vpot[ia,ib] = gauss_scale*(gaussian(dist1,0.0,sigma) + gaussian(dist2,0.0,sigma))

vpot_3d = np.zeros([na,nb,nc])
for ic in range(nc):
    vpot_3d[:,:,ic] = vpot

norb = len(orb_cube_list)
Vmat = np.zeros([norb,norb])
for iorb in range(norb):
    cube_i = orb_cube_list[iorb]
    for jorb in range(iorb,norb):
        cube_j = orb_cube_list[jorb]
        Vmat[iorb,jorb] = np.sum(cube_i*cube_j*vpot_3d)
        Vmat[jorb,iorb] = Vmat[iorb,jorb]

print('\nVmat:')
print(Vmat)

eigval,eigvec = np.linalg.eigh(Vmat)
print(f'Eigval of Vmat: {eigval}')
print('Eigvec:')
print(eigvec)
for isymorb in range(norb):
    symorb_cube = np.zeros([na,nb,nc])
    for iorb in range(norb):
        symorb_cube += orb_cube_list[iorb]*eigvec[iorb,isymorb]

    filnam = 'Symorb' + str(isymorb)+'.cube'
    write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,symorb_cube,'\n')
