import sys
from utils_holprt import *


list_adiabs = []
f = open('E_state_VBMG_to_CBMM.dat','r')
file_data = f.readlines()
for line in file_data:
    state = int(line.split()[0])
    state += 1
   #print(state)
    list_adiabs.append(state)

f.close()

#list of reference states is a 4-fold nested list
#The outer most list contains a list of reference groups. 
#Each reference group is a list of one or several states. Each reference group forms the 2nd outer most list.
#Each state forms the third outer most list. It is a list of hole-particle pairs and amplitudes.
#Each set of hole-pariticle pair and amplitude forms the inner most list. In order, it contains the cube files of the hole and particle orbitals, and the amplitude.

list_ref_states=[]


#State 0
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 1
ref_state_hp = ['VBM_G_layer1_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 2
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 3
ref_state_hp = ['VBM_G_layer2_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 4
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 5
ref_state_hp = ['VBM_G_layer3_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 6
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 7
ref_state_hp = ['VBM_G_layer4_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 8
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 9
ref_state_hp = ['VBM_G_layer5_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 10
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 11
ref_state_hp = ['VBM_G_layer6_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 12
ref_state_hp1 = ['VBM_G_layer1_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 13
ref_state_hp1 = ['VBM_G_layer1_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 14
ref_state_hp1 = ['VBM_G_layer2_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 15
ref_state_hp1 = ['VBM_G_layer2_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 16
ref_state_hp1 = ['VBM_G_layer3_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 17
ref_state_hp1 = ['VBM_G_layer3_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 18
ref_state_hp1 = ['VBM_G_layer4_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 19
ref_state_hp1 = ['VBM_G_layer4_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 20
ref_state_hp1 = ['VBM_G_layer5_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 21
ref_state_hp1 = ['VBM_G_layer5_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 22
ref_state_hp1 = ['VBM_G_layer6_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 23
ref_state_hp1 = ['VBM_G_layer6_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 24
ref_state_hp1 = ['VBM_G_layer1_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_sym.cube','CBM_M_layer6_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 25
ref_state_hp1 = ['VBM_G_layer1_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_antisym.cube','CBM_M_layer6_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 26
ref_state_hp1 = ['VBM_G_layer2_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_sym.cube','CBM_M_layer1_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 27
ref_state_hp1 = ['VBM_G_layer2_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_antisym.cube','CBM_M_layer1_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 28
ref_state_hp1 = ['VBM_G_layer3_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_sym.cube','CBM_M_layer2_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 29
ref_state_hp1 = ['VBM_G_layer3_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_antisym.cube','CBM_M_layer2_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 30
ref_state_hp1 = ['VBM_G_layer4_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_sym.cube','CBM_M_layer3_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 31
ref_state_hp1 = ['VBM_G_layer4_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_antisym.cube','CBM_M_layer3_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 32
ref_state_hp1 = ['VBM_G_layer5_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_sym.cube','CBM_M_layer4_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 33
ref_state_hp1 = ['VBM_G_layer5_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_antisym.cube','CBM_M_layer4_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 34
ref_state_hp1 = ['VBM_G_layer6_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_sym.cube','CBM_M_layer5_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 35
ref_state_hp1 = ['VBM_G_layer6_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_antisym.cube','CBM_M_layer5_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 36
ref_state_hp1 = ['VBM_G_layer1_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 37
ref_state_hp1 = ['VBM_G_layer1_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 38
ref_state_hp1 = ['VBM_G_layer2_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 39
ref_state_hp1 = ['VBM_G_layer2_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 40
ref_state_hp1 = ['VBM_G_layer3_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 41
ref_state_hp1 = ['VBM_G_layer3_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 42
ref_state_hp1 = ['VBM_G_layer4_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 43
ref_state_hp1 = ['VBM_G_layer4_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 44
ref_state_hp1 = ['VBM_G_layer5_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 45
ref_state_hp1 = ['VBM_G_layer5_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 46
ref_state_hp1 = ['VBM_G_layer6_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 47
ref_state_hp1 = ['VBM_G_layer6_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 48
ref_state_hp1 = ['VBM_G_layer1_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_sym.cube','CBM_M_layer5_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 49
ref_state_hp1 = ['VBM_G_layer1_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer1_antisym.cube','CBM_M_layer5_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 50
ref_state_hp1 = ['VBM_G_layer2_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_sym.cube','CBM_M_layer6_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 51
ref_state_hp1 = ['VBM_G_layer2_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer2_antisym.cube','CBM_M_layer6_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 52
ref_state_hp1 = ['VBM_G_layer3_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_sym.cube','CBM_M_layer1_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 53
ref_state_hp1 = ['VBM_G_layer3_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer3_antisym.cube','CBM_M_layer1_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 54
ref_state_hp1 = ['VBM_G_layer4_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_sym.cube','CBM_M_layer2_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 55
ref_state_hp1 = ['VBM_G_layer4_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer4_antisym.cube','CBM_M_layer2_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 56
ref_state_hp1 = ['VBM_G_layer5_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_sym.cube','CBM_M_layer3_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 57
ref_state_hp1 = ['VBM_G_layer5_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer5_antisym.cube','CBM_M_layer3_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 58
ref_state_hp1 = ['VBM_G_layer6_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_sym.cube','CBM_M_layer4_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 59
ref_state_hp1 = ['VBM_G_layer6_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state_hp2 = ['VBM_G_layer6_antisym.cube','CBM_M_layer4_kmesh220.cube',-1.0]
ref_state = [ref_state_hp1,ref_state_hp2]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 60
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 61
ref_state_hp = ['VBM_G_layer1_antisym.cube','CBM_M_layer4_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 62
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 63
ref_state_hp = ['VBM_G_layer2_antisym.cube','CBM_M_layer5_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 64
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 65
ref_state_hp = ['VBM_G_layer3_antisym.cube','CBM_M_layer6_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 66
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 67
ref_state_hp = ['VBM_G_layer4_antisym.cube','CBM_M_layer1_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 68
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 69
ref_state_hp = ['VBM_G_layer5_antisym.cube','CBM_M_layer2_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 70
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 71
ref_state_hp = ['VBM_G_layer6_antisym.cube','CBM_M_layer3_kmesh220.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

list_group_diabs_start_ind = [0,12,24,36,48,60]

list_group_diabs_properties = [0.0,9.5142035,9.5142035,19.0284070,19.0284070,28.5426105]

small = 0.1
lwrite = False
cp2k_output = 'SiH_4X4X6.out'
#Reference energy in hartree for all diagonal Hamiltonian elements
Eref = -867.04840080352540

diabatize_states(list_adiabs,list_ref_states,cp2k_output,Eref,small,list_group_diabs_start_ind,list_group_diabs_properties,lwrite)
