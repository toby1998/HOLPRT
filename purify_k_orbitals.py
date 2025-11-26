from utils_holprt import *
import sys

"""
Example of syntax: python purify_k_orbitals.py 3 CBM_M_layer1_0.cube CBM_M_layer1_1.cube CBM_M_layer1_2.cube 4 4 1 2 0 0 CBM_M_layer1_kmesh
"""

norb_input = int(sys.argv[1])

list_input_cube_files = []
for i in range(2,2+norb_input):
    filnam_input = sys.argv[i]
    list_input_cube_files.append(filnam_input)

ncell = np.array([0,0,0])
for i in range(3):
    ncell[i] = int(sys.argv[i+2+norb_input])

kmesh = np.array([0,0,0])
for i in range(3):
    kmesh[i] = int(sys.argv[i+5+norb_input])

cubefile_output = sys.argv[-1]
for i in range(3):
    cubefile_output += str(kmesh[i])

cubefile_output += '.cube'

#print(list_input_cube_files)
#print(ncell)
#print(kmesh)

#list_input_cube_files = ['CBM_M_layer1_0.cube','CBM_M_layer1_1.cube','CBM_M_layer1_2.cube']
#ncell = np.array([4,4,1])
#kmesh = np.array([2,0,0])
#kmesh / ncell gives the k grids. E.g., kmesh = [2,2,0] and ncell = [4,4,1] gives k = [1/2, 1/2, 0]
purify_k_orbitals(list_input_cube_files,ncell,kmesh,cubefile_output)
