import sys
from utils_holprt import *

cubefile = sys.argv[1]
ncell = np.array([1,1,1])
for i in range(3):
    ncell[i] = int(sys.argv[i+2])

print(f'Read in ncell: {ncell}')

print(cubefile)
#print(ncell)
natoms,crdorg,kabc,abc_grid,iatsrl,crdatm,cube_grid = read_cube_file(cubefile,True)
#ncell = np.array([4,4,1])
#getK_orbital(cubefile,True,ncell)
klist = getK_orbital(kabc,abc_grid,cube_grid,ncell)
for i in range(len(klist)):
    print(klist[i][0],np.around(klist[i][1],4))
