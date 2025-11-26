import sys
from utils_holprt import *


#Test of obtaining natural local hole/part orbitals for one state Start
outfile = 'SiH_4X4X1.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile,small=0.05)
#states_list = [1,2,3,4,5,6,7,8]
states_list=[]
for ist in range(1,21):
    states_list.append(ist)
list_read_orbs=[]
list_read_cube=[]
for state in states_list:
    print(f'\nWorking on State {state}')
    istate = state - 1
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat,list_read_orbs,list_read_cube = trnden_1state(ihole[istate],ipart[istate],cicoef[istate],list_read_orbs,list_read_cube)
    thrsh = 0.02
    for i,amplitude in enumerate(sglval):
        if amplitude > thrsh:
            filnam = 'NHO'+str(i)+'_state'+str(state)+'.cube'
            line2_text = 'Amplitude = ' + str(amplitude) + '\n'
            write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,orbhol_nat[i],line2_text)
            filnam = 'NPO'+str(i)+'_state'+str(state)+'.cube'
            write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,orbprt_nat[i],line2_text)
    
               #filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_locnathol' + str(ipair) + '.cube'
               #write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natholorb[ipair],'\n')
