import sys
from utils_holprt import *


#Test of obtaining natural local hole/part orbitals for one state Start
outfile = 'SiH_4X4X6.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile)
#zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#zlayer for SiH(1H)
zlayer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
#bright_states = [5,6,7,8,9,10,81,94,99,100,101,102,103,104,131,135,209,120]
list_read_cmo_ind = []
list_read_cmo_cube = []
states_of_interest = [11,12]
for state in states_of_interest:
    print(f'\nWorking on State {state}')
    istate = state - 1
    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat, list_read_cmo_ind, list_read_cmo_cube \
        = trnden_1state(ihole[istate],ipart[istate],cicoef[istate],list_read_cmo_ind,list_read_cmo_cube)
    prthrsh = 0.3
    #for ilayer in range(1,7):
    for ilayer in range(1,7):
        list_points = layer_of_integration(abc_grid,kabc,ilayer,zlayer,False)
        list_of_natholorb,list_of_prjprtorb = local_natural_holprt_layer(sglval,orbhol_nat,orbprt_nat,list_points,'LOCAL_NATURAL_HOLE')
        for ipair in range(len(list_of_prjprtorb)):
            prjnorm = np.sqrt(np.sum(list_of_prjprtorb[ipair]*list_of_prjprtorb[ipair]))
            if prjnorm > prthrsh:
                filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_locnathol' + str(ipair) + '.cube'
                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natholorb[ipair],'\n')
                filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_prjprt' + str(ipair) + '.cube'
                Line2_text = 'The norm of the projected orbital is ' + str(prjnorm) + '\n'
                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_prjprtorb[ipair],Line2_text)
            
        list_of_natprtorb,list_of_prjholorb = local_natural_holprt_layer(sglval,orbhol_nat,orbprt_nat,list_points,'LOCAL_NATURAL_PART')
        for ipair in range(len(list_of_prjprtorb)):
            prjnorm = np.sqrt(np.sum(list_of_prjholorb[ipair]*list_of_prjholorb[ipair]))
            if prjnorm > prthrsh:
                filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_locnatprt' + str(ipair) + '.cube'
                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natprtorb[ipair],'\n')
                filnam = 'State' + str(state) + '_Layer' + str(ilayer) + '_prjhol' + str(ipair) + '.cube'
                Line2_text = 'The norm of the projected orbital is ' + str(prjnorm) + '\n'
                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_prjholorb[ipair],Line2_text)
#Test of obtaining natural local hole/part orbitals for one state End
