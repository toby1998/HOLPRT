import sys
from utils_holprt import *


#Test of obtaining natural local hole/part orbitals for one state Start
outfile = 'SiH_4X4X1.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile,small=0.03)
states_list = [1,2,3,4,5,6,7,8]
#states_list = [1,2,3]
list_read_orbs=[]
list_read_cube=[]
list_key_orbitals = [79,80,81,82,83,84]
#remove the excitation scheme with orbitals not in list_key_orbitals
for state in states_list:
    istate = state - 1
    print(f'state : {state}')
    print(ihole[istate])
    print(ipart[istate])
    print(cicoef[istate])
    print(len(cicoef[istate]),len(ihole[istate]),len(ipart[istate]))
    for ihp_pair in range(len(cicoef[istate])-1,-1,-1):
        if ihole[istate][ihp_pair] not in list_key_orbitals or ipart[istate][ihp_pair] not in list_key_orbitals:
            del ihole[istate][ihp_pair]
            del ipart[istate][ihp_pair]
            del cicoef[istate][ihp_pair]
    print(f'state : {state} after cleaning')
    print(ihole[istate])
    print(ipart[istate])
    print(cicoef[istate])
    print(len(cicoef[istate]),len(ihole[istate]),len(ipart[istate]))

orthonormalize_trimmed_adiabats(ihole,ipart,cicoef,states_list)

for state in states_list:
    print(f'\nWorking on State {state}')
    istate = state - 1
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat,list_read_orbs,list_read_cube = trnden_1state(ihole[istate],ipart[istate],cicoef[istate],list_read_orbs,list_read_cube)
    thrsh = 0.05
    for i,amplitude in enumerate(sglval):
        if amplitude > thrsh:
            filnam = 'NHO'+str(i)+'_state'+str(state)+'.cube'
            line2_text = 'Amplitude = ' + str(amplitude) + '\n'
            write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,orbhol_nat[i],line2_text)
            filnam = 'NPO'+str(i)+'_state'+str(state)+'.cube'
            write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,orbprt_nat[i],line2_text)
    
               #filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_locnathol' + str(ipair) + '.cube'
               #write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natholorb[ipair],'\n')
