import sys
from utils_holprt import *

cp2k_output = sys.argv[1]
index_state = int(sys.argv[2])

ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(cp2k_output)

#index_state=0 #0 for 1st state
natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat, list_read_cmo, list_read_cmo_cube = \
   trnden_1state(ihole[index_state],ipart[index_state],cicoef[index_state])

# zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
# zlayer for SiH(6R)
#zlayer = [4.731188,14.193448,23.656,33.1182680,42.580536,52.043088]
# zlayer for SiH(1H)
zlayer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
# zlayer for SiH(3R)
#zlayer = [4.68978,14.0690585,23.448337,32.8278965,42.207175,51.586453]

#for layer in range(len(zlayer)):
#    ilayer = layer + 1
#    list_points_intgrl = layer_of_integration(abc_grid,kabc,ilayer,zlayer,True)

list_list_points = []

for ilayer in range(1,len(zlayer)+1):
    list_points = layer_of_integration(abc_grid,kabc,ilayer,zlayer,True)
    list_list_points.append(list_points)

holprt_tag = 'HOLE'

CT_nlayer = 0.0
accumul_prob = 0.0
for ilayer in range(1,len(zlayer)+1):
    cond_part_density = conditional_holprt_density(sglval,orbhol_nat,orbprt_nat,list_list_points[ilayer-1],holprt_tag)
   #filnam = 'state_' + str(index_state+1)+ '_conditional_' + holprt_tag + '_layer' + str(ilayer) + '.cube'
   #write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cond_part_density,'\n')
   #for jlayer in range(1,len(zlayer)+1):
   #    ic_init  = list_list_points[jlayer-1][ 0][2]
   #    ic_final = list_list_points[jlayer-1][-1][2]
   #    int_prob = np.sum(cond_part_density[:,:,ic_init:ic_final])
    for layer_ct in range(-2,4):
        jlayer = ilayer + layer_ct
        if jlayer <= 0: jlayer += len(zlayer)
        if jlayer > len(zlayer): jlayer -= len(zlayer)
        ic_init  = list_list_points[jlayer-1][ 0][2]
        ic_final = list_list_points[jlayer-1][-1][2]
        int_prob = np.sum(cond_part_density[:,:,ic_init:ic_final])
        accumul_prob += int_prob
        CT_nlayer += abs(layer_ct)*int_prob

print(f'Accumulated probability: {accumul_prob}, should be close to 1')
print(f'Average # of CT layers: {CT_nlayer}')        
