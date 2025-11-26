import sys
from utils_holprt import *

output_file = sys.argv[1]

ihole, ipart, cicoef,  osc_list, Eorb, Estate, E_scf = read_cp2k_output(output_file)
#hole orbitals for VBM_G-ML x 2 for SiH 1H hse06, SiH 3R hse06, and SiH 6R hse06
list_hole_pdos = []
for hole in range(469,481):
    list_hole_pdos.append(hole)
#part orbitals for CBM_G-ML for SiH 3R 6 layers vac hse06
#list_part_to_CBM_G = [485,488,489,493,494,495]
#part orbitals for CBM_M-ML for SiH 1H 6 layers vac hse06
#list_part_pdos = [485,488,489,493,494,495]
#part orbitals for CBM_G-ML for SiH 6R 6 layers vac hse06
#list_part_pdos = [481,482,492,502,503,504]
#list_part_pdos = []
#for part in range(481,504+1):
#    if part not in list_part_to_remove:
#        list_part_pdos.append(part)
#list_part_pdos = list(set(list_part_pdos) - set(list_part_to_remove))

#part orbitals for CBM_G-ML for SiH 1H hse06
#list_part_pdos = [481,482,483,502,503,504]
#part orbitals for CBM_M-ML for SiH 1H hse06
#list_part_pdos = []
#for part in range(484,502):
#    list_part_pdos.append(part)

#part orbitals for CBM_G-ML for SiH 3R hse06
#list_part_pdos = [484,489,491,493,494,495]
#part orbitals for CBM_M-ML for SiH 3R hse06
#list_part_pdos = [481,482,483,485,486,487,488,490,492,496,497,498,499,500,501,502,503,504]

#part orbitals for CBM_G-ML for SiH 6R hse06
#list_part_pdos = [481,482,483,502,503,504]
#part orbitals for CBM_M-ML for SiH 6R hse06
#list_part_pdos = []
#for part in range(484,502):
#    list_part_pdos.append(part)

#VBM_G of SiH_ML
#list_hole_pdos = [79,80]
#CBM_G of SiH_ML
#list_part_pdos = [81]
#CBM_M of SiH_ML
#list_part_pdos = [82,83,84]

list_part_pdos = []
for orb in range(481,487):
    list_part_pdos.append(orb)

tddft_dos(Estate,ihole,ipart,cicoef,list_hole_pdos=list_hole_pdos,list_part_pdos=list_part_pdos,debug=False)
