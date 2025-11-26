import sys
from utils_holprt import *

#filnam = sys.argv[1]

#file_exists(filnam)

#natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(filnam)
#write_cube_file('test.cube',natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid)

##Test of constructing transition density matrix start
#ihole, ipart, cicoef,  osc, Eorb = read_cp2k_output(filnam)

#istate=0
#natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat = trnden_1state(ihole[istate],ipart[istate],cicoef[istate])
#Test of constructing transition density matrix end

#natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(filnam)
# zlayer for SiH(1H)
#layer = [4.7572445,14.271448,23.7856515,33.3001405,42.814344,52.3285475]
# zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#for ilayer in range(1,7):
   #list_points_intgrl = layer_of_integration(abc_grid,kabc,ilayer,zlayer,True)
##Test of constructing transition density matrix end

##Test of localizing orbitals start

#orb_list = []
#orb_cube_list = []
#for iorb in range(469,481):
#    orb_list.append(iorb)
#    cubefile = str(iorb) + '.cube'
#    file_exists(cubefile)
#    print(f'Reading {cubefile}')
#    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(cubefile)
#    orb_cube_list.append(cube_grid)
#    
#
#
## zlayer for SiH(1H) 6 layers + vacuum
#zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#for layer in range(len(zlayer)):
#    ilayer = layer + 1
#    list_points_intgrl = layer_of_integration(abc_grid,kabc,ilayer,zlayer,False)
#
#    n_locorb, locorb_cube = localize_orbitals(orb_list,orb_cube_list,list_points_intgrl)
#    for locorb in range(n_locorb):
#        filnam = 'LOCORB_layer' + str(ilayer) + '_' + str(locorb) + '.cube'
#        write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,locorb_cube[locorb])
##Test of localizing orbitals end

#Test of projecting a hole orbital onto the density matrix to get its associated particle orbital Start
#outfile = 'SiH_4X4X6.out'
#ihole, ipart, cicoef,  osc_list, Eorb, Estate = read_cp2k_output(outfile)
#f = open("CT_dist.txt", "w")
#f.write(" State   Energy      OSC           Norm Orb.   Layer weights                                                           CT dist / Angs"+"\n")
#for state in range(1,501):
#    istate = state -1
#    if osc_list[istate] > 0.1 :
#        print(f'\nWorking on State {state}')
#        natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat = trnden_1state(ihole[istate],ipart[istate],cicoef[istate])
#        holcubefile = 'LOCORB_layer3_1.cube'
#        projected_hole_cube = holprt_proj_trnden(holcubefile,sglval,orbhol_nat,orbprt_nat,'HOLPRJ2PRT')
#       # zlayer for SiH(1H) 6 layers + vacuum
#        zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#        initlayer=1
#        Lpbc = False
#        dnorm = np.sqrt(np.sum(projected_hole_cube*projected_hole_cube))
#        small = 0.1
#        if dnorm > small:
#            CTdist, layer_weights = layer_CT_distance(projected_hole_cube,zlayer,initlayer,abc_grid,kabc,crdorg,Lpbc)
#          # print("{:4d} {:12.6f}*10 \n".format(state,Estate[istate],osc_list[istate],layer_weights))
#            print("".join(f"{state:4d} {Estate[istate]:12.6f} {osc_list[istate]:12.6f} {dnorm:12.6f}"),end='')
#            print("".join(f"{elm:12.6f}" for elm in layer_weights),end='')
#            print("".join(f"{CTdist:12.6f}"))
#            f.write("".join(f"{state:4d} {Estate[istate]:12.6f} {osc_list[istate]:12.6f} {dnorm:12.6f}"))
#            f.write("".join(f"{elm:12.6f}" for elm in layer_weights))
#            f.write("".join(f"{CTdist:12.6f}") + "\n")
#
#f.close()
##Test of projecting a hole orbital onto the density matrix to get its associated particle orbital End

#Test of obtaining natural local hole/part orbitals for one state Start
#outfile = 'SiH_4X4X6.out'
#ihole, ipart, cicoef,  osc_list, Eorb, Estate = read_cp2k_output(outfile)
#bright_states = [1,2]
#for state in bright_states:
#    print(f'\nWorking on State {state}')
#    istate = state - 1
#    natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat = trnden_1state(ihole[istate],ipart[istate],cicoef[istate])
#   #zlayer for SiH(1H) 6 layers + vacuum
#    zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]
#    prthrsh = 0.5
#    #for ilayer in range(1,7):
#    for ilayer in range(1,7):
#        list_points = layer_of_integration(abc_grid,kabc,ilayer,zlayer,False)
#        list_of_natholorb,list_of_prjprtorb = local_natural_holprt_layer(sglval,orbhol_nat,orbprt_nat,list_points,'LOCAL_NATURAL_HOLE')
#        for ipair in range(len(list_of_prjprtorb)):
#            prjnorm = np.sqrt(np.sum(list_of_prjprtorb[ipair]*list_of_prjprtorb[ipair]))
#            if prjnorm > prthrsh:
#                filnam = 'State' + str(istate+1) + '_Layer' + str(ilayer) + '_locnathol' + str(ipair) + '.cube'
#                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natholorb[ipair],'\n')
#                filnam = 'State' + str(istate+1) + '_Layer' + str(ilayer) + '_prjprt' + str(ipair) + '.cube'
#                Line2_text = 'The norm of the projected orbital is ' + str(prjnorm) + '\n'
#                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_prjprtorb[ipair],Line2_text)
#            
#        list_of_natprtorb,list_of_prjholorb = local_natural_holprt_layer(sglval,orbhol_nat,orbprt_nat,list_points,'LOCAL_NATURAL_PART')
#        for ipair in range(len(list_of_prjprtorb)):
#            prjnorm = np.sqrt(np.sum(list_of_prjholorb[ipair]*list_of_prjholorb[ipair]))
#            if prjnorm > prthrsh:
#                filnam = 'State' + str(istate+1) + '_Layer' + str(ilayer) + '_locnatprt' + str(ipair) + '.cube'
#                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_natprtorb[ipair],'\n')
#                filnam = 'State' + str(istate+1) + '_Layer' + str(ilayer) + '_prjhol' + str(ipair) + '.cube'
#                Line2_text = 'The norm of the projected orbital is ' + str(prjnorm) + '\n'
#                write_cube_file(filnam,natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,list_of_prjholorb[ipair],Line2_text)
##Test of obtaining natural local hole/part orbitals for one state End

#Test of getting local orbitals' energies Start
outfile = 'SiH_4X4X6.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate = read_cp2k_output(outfile)
canon_list = []
canon_cube_list = []
for iorb in range(469,480+1):
    canon_list.append(iorb)

locorb_cubefile_list = ['LOCORB_layer1_0.cube','LOCORB_layer1_1.cube','LOCORB_layer2_0.cube','LOCORB_layer2_1.cube','LOCORB_layer3_0.cube','LOCORB_layer3_1.cube','LOCORB_layer4_0.cube','LOCORB_layer4_1.cube','LOCORB_layer5_0.cube','LOCORB_layer5_1.cube','LOCORB_layer6_0.cube','LOCORB_layer6_1.cube']
#locorb_cubefile = 'State10_Layer1_prjprt0.cube'
#locorb_cubefile_list.append(locorb_cubefile)

get_Hmat_locorb(canon_list,locorb_cubefile_list,Eorb)

#Test of getting local orbitals' energies End
