import sys
from utils_holprt import *

##Test of localizing orbitals start

orb_list = []
#for iorb in range(469,481):
#for iorb in range(481,487):
for iorb in range(487,505):
    orb_list.append(iorb)
#orb_list = [481,482,483,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504]
#orb_list = [484,485,486,487,488,489]
#CBMG-ML orbitals in SiH 1H 6 layers vac
#orb_list= [481,482,492,499,503,504]
#CBMG-ML orbitals in SiH 3R 6 layers vac
#orb_list_CBMG= [485,488,489,493,494,495]
#CBMG-ML orbitals in SiH 6R 6 layers vac
#list_orb_to_remove = [481,482,492,502,503,504]
#CBMG-ML orbitals in SiH 6R
#orb_list = [481,482,483,502,503,504]
#orb_list = []
#for iorb in range(481,505):
#    if iorb not in orb_list_CBMG:
#        orb_list.append(iorb)
#part orbitals for CBM_M-ML for SiH 1H 6 layers vac hse06
#part orbitals for CBM_G-ML for SiH(3R)
#orb_list = [484,489,491,493,494,495]
#list_orb_to_remove = [484,489,491,493,494,495]
#list_all_orbs = []
#for orb in range(481,504+1):
#    list_all_orbs.append(orb)
#orb_list = list(set(list_all_orbs) - set(list_orb_to_remove))
orb_cube_list = []
for iorb in orb_list:
    cubefile = str(iorb) + '.cube'
    file_exists(cubefile)
    print(f'Reading {cubefile}')
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(cubefile,True)
    orb_cube_list.append(cube_grid)



# zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
# zlayer for SiH(6R)
#zlayer = [9.4622680,18.9248200,28.3870880,37.8493560,47.3119080,56.77417385555148]
# zlayer for SiH(6R) 6 layers vac
#zlayer = [4.344959,13.807503,23.270047,32.732591,42.195135,51.657206]
# zlayer for SiH(1H)
#zlayer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
#zlayer for SiH(3R)
#zlayer = [4.68978,14.0690585,23.448337,32.8278965,42.207175,51.586453]
#zlayer for SiH(3R) 6 layers + vacuum
#zlayer = [4.689897,14.0687508,23.448545,32.8278692,42.207193,51.586517]
# zlayers for GeH(6R)
#zlayer = [9.256526005,18.5131915,27.769856,37.026521,46.2831875,55.5397175]
# zlayers for GeH(1H)
#zlayer = [9.227215,18.4544305,27.6816455,36.9088615,46.1360745,55.363305]
# zlayers for GeH(3R)
zlayer = [4.544663,13.634003,22.72333,31.8126695,40.902009,49.991336]
dsum_accumulate = 0.0
for layer in range(len(zlayer)):
    ilayer = layer + 1
    list_points_intgrl = layer_of_integration(abc_grid,kabc,ilayer,zlayer,Lpbc=False)

   #dsum = 0.0
   #for ipoint in range(len(list_points_intgrl)):
   #    ia = list_points_intgrl[ipoint][0]
   #    ib = list_points_intgrl[ipoint][1]
   #    ic = list_points_intgrl[ipoint][2]
   #    dsum += orb_cube_list[0][ia,ib,ic]*orb_cube_list[0][ia,ib,ic]

   #dsum_accumulate += dsum
   #print(f'\nLayer {ilayer} integration gives {dsum}, accumulated integral: {dsum_accumulate}')

    n_locorb, locorb_cube = localize_orbitals(orb_list,orb_cube_list,list_points_intgrl)
    for locorb in range(n_locorb):
        filnam = 'LOCORB_layer' + str(ilayer) + '_' + str(locorb) + '.cube'
        write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,locorb_cube[locorb],'\n')
##Test of localizing orbitals end
