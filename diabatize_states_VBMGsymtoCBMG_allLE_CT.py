import sys
from utils_holprt import *


list_adiabs = []
f = open('E_state_VBMG_to_CBMG.dat','r')
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
#list_ref_states = [[[['../VBMG_antisym_longaxis_with_CBMM220.cube','../CBM_M_kmesh220.cube',1.0]]],[[['../VBMG_antisym_axis120_with_CBMM020.cube','../CBM_M_kmesh020.cube',1.0]]],[[['../VBMG_antisym_axis240_with_CBMM200.cube','../CBM_M_kmesh200.cube',1.0]]],[[['../VBMG_antisym_longaxis_with_CBMM220.cube','../CBM_G.cube',1.0]]],[[['../VBMG_sym_longaxis_with_CBMM220.cube','../CBM_G.cube',1.0]]],[[['../VBMG_sym_longaxis_with_CBMM220.cube','../CBM_M_kmesh220.cube',1.0]]],[[['../VBMG_sym_axis120_with_CBMM020.cube','../CBM_M_kmesh020.cube',1.0]]],[[['../VBMG_sym_axis240_with_CBMM200.cube','../CBM_M_kmesh200.cube',1.0]]]]
#list_ref_states = [[[['./VBMG_antisym_longaxis_with_CBMM220.cube','./CBM_M_kmesh220.cube',1.0]]],[[['./VBMG_antisym_axis120_with_CBMM020.cube','./CBM_M_kmesh020.cube',1.0]]],[[['./VBMG_antisym_axis240_with_CBMM200.cube','./CBM_M_kmesh200.cube',1.0]]],[[['./VBMG_antisym_longaxis_with_CBMM220.cube','./CBM_G.cube',1.0]]],[[['./VBMG_sym_longaxis_with_CBMM220.cube','./CBM_G.cube',1.0]]],[[['./VBMG_sym_longaxis_with_CBMM220.cube','./CBM_M_kmesh220.cube',1.0]]],[[['./VBMG_sym_axis120_with_CBMM020.cube','./CBM_M_kmesh020.cube',1.0]]],[[['./VBMG_sym_axis240_with_CBMM200.cube','./CBM_M_kmesh200.cube',1.0]]]]
#list_ref_states = [[[['./NHO0_state1.cube','./NPO0_state1.cube',0.9975659541192681]]],[[['./NHO0_state2.cube','./NPO0_state1.cube',0.9843454710295532],['./NHO1_state2.cube','./NPO1_state2.cube',0.17624980471934384]]],[[['./NHO0_state3.cube','./NPO0_state3.cube',0.9999999999999999]]],[[['./NHO0_state4.cube','./NPO0_state4.cube',1.0]]],[[['./NHO0_state5.cube','./NPO0_state5.cube',1.0]]],[[['./NHO0_state6.cube','./NPO0_state6.cube',0.9999999999999998]]],[[['./NHO0_state7.cube','./NPO0_state7.cube',0.9935459708519536],['./NHO1_state7.cube','./NPO1_state7.cube',0.11343017148822823]]],[[['./NHO0_state8.cube','./NPO0_state8.cube',0.9899147562578214],['./NHO1_state8.cube','./NPO1_state8.cube',0.14166430511253905]]]]

list_ref_states=[]


#State 0
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 1
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 2
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 3
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 4
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 5
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 6
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 7
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 8
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 9
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 10
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 11
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 12
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 13
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 14
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 15
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 16
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 17
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 18
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 19
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 20
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 21
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 22
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 23
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 24
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 25
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 26
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 27
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 28
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 29
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 30
ref_state_hp = ['VBM_G_layer1_sym.cube','CBM_G_layer4_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 31
ref_state_hp = ['VBM_G_layer2_sym.cube','CBM_G_layer5_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 32
ref_state_hp = ['VBM_G_layer3_sym.cube','CBM_G_layer6_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 33
ref_state_hp = ['VBM_G_layer4_sym.cube','CBM_G_layer1_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 34
ref_state_hp = ['VBM_G_layer5_sym.cube','CBM_G_layer2_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)

#State 35
ref_state_hp = ['VBM_G_layer6_sym.cube','CBM_G_layer3_0.cube',1.0]
ref_state = [ref_state_hp]
ref_group = [ref_state]

list_ref_states.append(ref_group)


small = 0.1
lwrite = False
cp2k_output = 'SiH_4X4X6.out'
#Reference energy in hartree for all diagonal Hamiltonian elements
Eref = -867.04840080352540

diabatize_states(list_adiabs,list_ref_states,cp2k_output,Eref,small,lwrite)
