import sys
from utils_holprt import *


outfile = 'SiH_4X4X1.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile,small=0.05)

states_to_exclude = [1,2,3,4,9,11,13,14,24,25,26,27]
state_list = []
for istate in range(1,30+1):
    if istate not in states_to_exclude:
        state_list.append(istate)

for state in state_list:
    istate = state - 1
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat, list_read_cmo_idx, list_read_cmo_cube = trnden_1state(ihole[istate],ipart[istate],cicoef[istate])

    partcube = 'CBM_M_layer1_kmesh220'
    partcubefile = partcube + '.cube'
    holfilname = 'State' + str(state) + '_' + partcube + '_projected_hole.cube'
    projected_hole_cube = holprt_proj_trnden(partcubefile,sglval,orbhol_nat,orbprt_nat,'PRTPRJ2HOL',holfilname)
