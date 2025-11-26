from utils_holprt import *

######## Setting for SiH(1H) #####################
hole_canon_list = []
for iorb in range(469,481):
    hole_canon_list.append(iorb)

print(f'list of canonical hole orbitals under consideration')
print(hole_canon_list)

part_canon_list = [484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,501,502,503]
print(f'list of canonical particle orbitals under consideration')
print(part_canon_list)

local_hole_cube_file_list = ['VBM_G_layer1_antisym.cube']
local_part_cube_file_list = ['CBM_M_layer1_kmesh220.cube','CBM_M_layer2_kmesh220.cube','CBM_M_layer3_kmesh220.cube','CBM_M_layer4_kmesh220.cube','CBM_M_layer5_kmesh220.cube','CBM_M_layer6_kmesh220.cube']

cp2k_output_file = 'SiH_1H_446.out'
######## Setting Done #############################


holprt_pair_energy(local_hole_cube_file_list,local_part_cube_file_list,hole_canon_list,part_canon_list,cp2k_output_file)
