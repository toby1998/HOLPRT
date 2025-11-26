import sys
from utils_holprt import *


#Test of projecting a hole orbital onto the density matrix to get its associated particle orbital Start
outfile = 'SiH_4X4X6.out'
ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(outfile)
#initlayer=5
#holorb_of_initlayer = 1
#holcube = 'LOCORB_layer' + str(initlayer) + '_' + str(holorb_of_initlayer)
#holcubefile = holcube + '.cube'
#CTfile = holcube + '_CT_dist.txt'
CTfile = 'CT_dist.txt'
f = open(CTfile, "w")
f.write("#State   Energy      OSC       Layer Orb     Norm Orb.   Layer weights                                                           CT dist / Bohr" + "\n")
CTavrgdist_file  = 'CT_avrg_dist.txt'
fCTavrgdist = open(CTavrgdist_file, "w")
fCTavrgdist.write("#State   Energy      OSC           Norm Orb.        dCT / bohr"+"\n")

#parameters for plotting CT dist vs E in Gaussian broadening
Egrid_init = 2.9
Egrid_final = 4.0
nEgrid = 1000
Egrid_step = (Egrid_final - Egrid_init)/float(nEgrid)
Egrid = np.zeros([nEgrid])
CTdist_Egrid = np.zeros([nEgrid])
gausig = 0.005 #in eV^-1

# zlayer for SiH(1H) 6 layers + vacuum
zlayer = [4.757299,14.2714225,23.785546,33.300144,42.8142675,52.328391]

for iEgrid in range(nEgrid):
    Egrid[iEgrid] = Egrid_step*iEgrid + Egrid_init

nstate = len(Estate)
for state in range(1,nstate+1):
#for state in range(1,13):
    istate = state -1
    if osc_list[istate] > 0.1 :
        natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat = trnden_1state(ihole[istate],ipart[istate],cicoef[istate])
       #holcubefile = 'LOCORB_layer3_1.cube'
        dnorm_sum = 0.0
        CTdist_sum = 0.0
        for initlayer in range(1,7):
            for holorb_of_initlayer in range(2):
                print(f'\nWorking on State {state}, Layer {initlayer}, Hole orbital {holorb_of_initlayer}')
                holcube = 'LOCORB_layer' + str(initlayer) + '_' + str(holorb_of_initlayer)
                holcubefile = holcube + '.cube'
                prtfilname = holcube + '_state' + str(state) + '.cube' 
                projected_hole_cube = holprt_proj_trnden(holcubefile,sglval,orbhol_nat,orbprt_nat,'HOLPRJ2PRT',prtfilname)
                Lpbc = False
                dnorm = np.sqrt(np.sum(projected_hole_cube*projected_hole_cube))
                dnorm_sum += dnorm**2
                CTdist, layer_weights = layer_CT_distance(projected_hole_cube,zlayer,initlayer,abc_grid,kabc,crdorg,Lpbc)
                CTdist_sum += CTdist*dnorm**2
               #gaussian broadening of the CT distance
                for iEgrid in range(nEgrid):
                    CTdist_Egrid[iEgrid] +=  CTdist * gaussian(Egrid[iEgrid],Estate[istate],gausig)
                small = 0.1
                if dnorm > small:
                  # print("{:4d} {:12.6f}*10 \n".format(state,Estate[istate],osc_list[istate],layer_weights))
                    print("".join(f"{state:4d} {Estate[istate]:12.6f} {osc_list[istate]:12.6f} {initlayer:4d} {holorb_of_initlayer:4d} {dnorm:12.6f}"),end='')
                    print("".join(f"{elm:12.6f}" for elm in layer_weights),end='')
                    print("".join(f"{CTdist:12.6f}"))
                    f.write("".join(f"{state:4d} {Estate[istate]:12.6f} {osc_list[istate]:12.6f} {initlayer:4d} {holorb_of_initlayer:4d} {dnorm:12.6f}"))
                    f.write("".join(f"{elm:12.6f}" for elm in layer_weights))
                    f.write("".join(f"{CTdist:12.6f}") + "\n")
        
        dnorm_sum = np.sqrt(dnorm_sum)
        print(f'\ndnorm_sum = {dnorm_sum}, CTdist_sum = {CTdist_sum}')
        fCTavrgdist.write("".join(f"{state:4d} {Estate[istate]:12.6f} {osc_list[istate]:12.6f} {dnorm_sum:12.6f} {CTdist_sum:12.6f}") + "\n")
        
f.close()
fCTavrgdist.close()
CTdist_E_profile = 'CTdist_E.txt'
f = open(CTdist_E_profile, 'w')
f.write("#E in eV      CT dist in Bohr\n")
for iEgrid in range(nEgrid):
    f.write("".join(f"{Egrid[iEgrid]:12.6f} {CTdist_Egrid[iEgrid]:12.6f}" + "\n"))
#Test of projecting a hole orbital onto the density matrix to get its associated particle orbital End
