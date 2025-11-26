import sys
from utils_holprt import *

cp2k_output = sys.argv[1]
ncell = np.array([1,1,1])
for i in range(3):
    ncell[i] = int(sys.argv[i+2])

istate = int(sys.argv[5])

ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(cp2k_output)

index_state = istate-1

natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,sglval,orbhol_nat,orbprt_nat = trnden_1state(ihole[index_state],ipart[index_state],cicoef[index_state])

print(f'\nAnalyzing k vector for state {istate}')
getK_TDstate(kabc,abc_grid,ncell,sglval,orbhol_nat,orbprt_nat)
