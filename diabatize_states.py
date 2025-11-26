import sys
from utils_holprt import *


list_adiabs = [1,2,3,4,5,6,7,8]
#list of reference states is a 4-fold nested list
#The outer most list contains a list of reference groups. 
#Each reference group is a list of one or several states. Each reference group forms the 2nd outer most list.
#Each state forms the third outer most list. It is a list of hole-particle pairs and amplitudes.
#Each set of hole-pariticle pair and amplitude forms the inner most list. In order, it contains the cube files of the hole and particle orbitals, and the amplitude.
#list_ref_states = [[[['../VBMG_antisym_longaxis_with_CBMM220.cube','../CBM_M_kmesh220.cube',1.0]]],[[['../VBMG_antisym_axis120_with_CBMM020.cube','../CBM_M_kmesh020.cube',1.0]]],[[['../VBMG_antisym_axis240_with_CBMM200.cube','../CBM_M_kmesh200.cube',1.0]]],[[['../VBMG_antisym_longaxis_with_CBMM220.cube','../CBM_G.cube',1.0]]],[[['../VBMG_sym_longaxis_with_CBMM220.cube','../CBM_G.cube',1.0]]],[[['../VBMG_sym_longaxis_with_CBMM220.cube','../CBM_M_kmesh220.cube',1.0]]],[[['../VBMG_sym_axis120_with_CBMM020.cube','../CBM_M_kmesh020.cube',1.0]]],[[['../VBMG_sym_axis240_with_CBMM200.cube','../CBM_M_kmesh200.cube',1.0]]]]
#list_ref_states = [[[['./VBMG_antisym_longaxis_with_CBMM220.cube','./CBM_M_kmesh220.cube',1.0]]],[[['./VBMG_antisym_axis120_with_CBMM020.cube','./CBM_M_kmesh020.cube',1.0]]],[[['./VBMG_antisym_axis240_with_CBMM200.cube','./CBM_M_kmesh200.cube',1.0]]],[[['./VBMG_antisym_longaxis_with_CBMM220.cube','./CBM_G.cube',1.0]]],[[['./VBMG_sym_longaxis_with_CBMM220.cube','./CBM_G.cube',1.0]]],[[['./VBMG_sym_longaxis_with_CBMM220.cube','./CBM_M_kmesh220.cube',1.0]]],[[['./VBMG_sym_axis120_with_CBMM020.cube','./CBM_M_kmesh020.cube',1.0]]],[[['./VBMG_sym_axis240_with_CBMM200.cube','./CBM_M_kmesh200.cube',1.0]]]]
#list_ref_states = [[[['./NHO0_state1.cube','./NPO0_state1.cube',0.9975659541192681]]],[[['./NHO0_state2.cube','./NPO0_state1.cube',0.9843454710295532],['./NHO1_state2.cube','./NPO1_state2.cube',0.17624980471934384]]],[[['./NHO0_state3.cube','./NPO0_state3.cube',0.9999999999999999]]],[[['./NHO0_state4.cube','./NPO0_state4.cube',1.0]]],[[['./NHO0_state5.cube','./NPO0_state5.cube',1.0]]],[[['./NHO0_state6.cube','./NPO0_state6.cube',0.9999999999999998]]],[[['./NHO0_state7.cube','./NPO0_state7.cube',0.9935459708519536],['./NHO1_state7.cube','./NPO1_state7.cube',0.11343017148822823]]],[[['./NHO0_state8.cube','./NPO0_state8.cube',0.9899147562578214],['./NHO1_state8.cube','./NPO1_state8.cube',0.14166430511253905]]]]

list_ref_states=[]
ref_state1_hp1 = ['../NHO0_state1.cube','../NPO0_state1.cube',0.9909450896536288]
ref_state1_hp2 = ['../NHO1_state1.cube','../NPO1_state1.cube',0.08592807506141587]
ref_state1_hp3 = ['../NHO2_state1.cube','../NPO2_state1.cube',0.08248651962074294]
ref_state1_hp4 = ['../NHO3_state1.cube','../NPO3_state1.cube',0.04909741654466081]
ref_state1_hp5 = ['../NHO4_state1.cube','../NPO4_state1.cube',0.03781022318233208]

ref_state1 = [ref_state1_hp1,ref_state1_hp2,ref_state1_hp3,ref_state1_hp4,ref_state1_hp5]
ref_group1 = [ref_state1]
list_ref_states.append(ref_group1)

ref_state2_hp1 = ['../NHO0_state2.cube','../NPO0_state2.cube',0.9862488872227679]
ref_state2_hp2 = ['../NHO1_state2.cube','../NPO1_state2.cube',0.11120778997014416]
ref_state2_hp3 = ['../NHO2_state2.cube','../NPO2_state2.cube',0.08263450559120626]
ref_state2_hp4 = ['../NHO3_state2.cube','../NPO3_state2.cube',0.08250913727294679]
ref_state2_hp5 = ['../NHO4_state2.cube','../NPO4_state2.cube',0.03619033923547862]

ref_state2 = [ref_state2_hp1,ref_state2_hp2,ref_state2_hp3,ref_state2_hp4,ref_state2_hp5]
ref_group2 = [ref_state2]
list_ref_states.append(ref_group2)

ref_state3_hp1 = ['../NHO0_state3.cube','../NPO0_state3.cube',0.9863494976851737]
ref_state3_hp2 = ['../NHO1_state3.cube','../NPO1_state3.cube',0.1102707691478273]
ref_state3_hp3 = ['../NHO2_state3.cube','../NPO2_state3.cube',0.08539519114052471]
ref_state3_hp4 = ['../NHO3_state3.cube','../NPO3_state3.cube',0.07968655994569705]
ref_state3_hp5 = ['../NHO4_state3.cube','../NPO4_state3.cube',0.03623174549819469]

ref_state3 = [ref_state3_hp1,ref_state3_hp2,ref_state3_hp3,ref_state3_hp4,ref_state3_hp5]
ref_group3 = [ref_state3]
list_ref_states.append(ref_group3)

ref_state4_hp1 = ['../NHO0_state4.cube','../NPO0_state4.cube',0.9927419533918488]
ref_state4_hp2 = ['../NHO1_state4.cube','../NPO1_state4.cube',0.05779891908293997]
ref_state4_hp3 = ['../NHO2_state4.cube','../NPO2_state4.cube',0.05401547574241249]
ref_state4_hp4 = ['../NHO3_state4.cube','../NPO3_state4.cube',0.05380587931107253]
ref_state4_hp5 = ['../NHO4_state4.cube','../NPO4_state4.cube',0.05368696891971441]
ref_state4_hp6 = ['../NHO5_state4.cube','../NPO5_state4.cube',0.03494506135541842]
ref_state4_hp7 = ['../NHO6_state4.cube','../NPO6_state4.cube',0.03473480553483634]

ref_state4 = [ref_state4_hp1,ref_state4_hp2,ref_state4_hp3,ref_state4_hp4,ref_state4_hp5,ref_state4_hp6,ref_state4_hp7]
ref_group4 = [ref_state4]
list_ref_states.append(ref_group4)

ref_state5_hp1 = ['../NHO0_state5.cube','../NPO0_state5.cube',0.9935593724463347]
ref_state5_hp2 = ['../NHO1_state5.cube','../NPO1_state5.cube',0.062013161833929874]
ref_state5_hp3 = ['../NHO2_state5.cube','../NPO2_state5.cube',0.06008541110762106]
ref_state5_hp4 = ['../NHO3_state5.cube','../NPO3_state5.cube',0.03667643599434379]
ref_state5_hp5 = ['../NHO4_state5.cube','../NPO4_state5.cube',0.03349228552345475]
ref_state5_hp6 = ['../NHO5_state5.cube','../NPO5_state5.cube',0.03264230901893441]
ref_state5_hp7 = ['../NHO6_state5.cube','../NPO6_state5.cube',0.030571055765888405]
ref_state5_hp8 = ['../NHO7_state5.cube','../NPO7_state5.cube',0.030280036655722053]

ref_state5 = [ref_state5_hp1,ref_state5_hp2,ref_state5_hp3,ref_state5_hp4,ref_state5_hp5,ref_state5_hp6,ref_state5_hp7,ref_state5_hp8]
ref_group5 = [ref_state5]
list_ref_states.append(ref_group5)

ref_state6_hp1 = ['../NHO0_state6.cube','../NPO0_state6.cube',0.9968438267679532]
ref_state6_hp2 = ['../NHO1_state6.cube','../NPO1_state6.cube',0.07938756221614734]

ref_state6 = [ref_state6_hp1,ref_state6_hp2]
ref_group6 = [ref_state6]
list_ref_states.append(ref_group6)

ref_state7_hp1 = ['../NHO0_state7.cube','../NPO0_state7.cube',0.9919017400256551]
ref_state7_hp2 = ['../NHO1_state7.cube','../NPO1_state7.cube',0.12700763021991018]

ref_state7 = [ref_state7_hp1,ref_state7_hp2]
ref_group7 = [ref_state7]
list_ref_states.append(ref_group7)

ref_state8_hp1 = ['../NHO0_state8.cube','../NPO0_state8.cube',0.9899147562578214]
ref_state8_hp2 = ['../NHO1_state8.cube','../NPO1_state8.cube',0.14166430511253905]

ref_state8 = [ref_state8_hp1,ref_state8_hp2]
ref_group8 = [ref_state8]
list_ref_states.append(ref_group8)


small = 0.02
lwrite = False
cp2k_output = 'SiH_4X4X1.out'
#Reference energy in hartree for all diagonal Hamiltonian elements
Eref = -144.43167219425342

diabatize_states(list_adiabs,list_ref_states,cp2k_output,Eref,small,lwrite)
