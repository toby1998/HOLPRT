import sys
#sys.path.append('/scratch/ekadashi/TEST_Cal/test_diabatization/TEST1/')
#from utils_holprt_main_upgrade import *
#from utils_holprt_main_optimized_debug import *
from utils_holprt_main_optimized_norepeat import *
#from code_optimized import *
#from utils_holprt_main import *

def expand_range(rng):
    lo, hi = rng
    return list(range(lo, hi + 1))

list_adiabs = []
for ist in range(1,9): list_adiabs.append(ist)

#orbdir='/scratch/ekadashi/TEST_Cal/test_diabatization/'
#orbdir='/project/rrg-tzeng/tz_eka/test_diabatization/'
orbdir='/scratch/ekadashi/TEST_CODES/PhonExD/TEST_diabatization/R0_c_CMOs/'
#/project/rrg-tzeng/tz_eka/test_diabatization
#orbdir='../'

list_ref_states=[]
ref_state1_hp1 = [orbdir+'NHO0_state1.cube',orbdir+'NPO0_state1.cube',0.9859610410728864]
ref_state1_hp2 = [orbdir+'NHO1_state1.cube',orbdir+'NPO1_state1.cube',0.1217758246467255]
ref_state1_hp3 = [orbdir+'NHO2_state1.cube',orbdir+'NPO2_state1.cube',0.0817130646680653]
ref_state1_hp4 = [orbdir+'NHO3_state1.cube',orbdir+'NPO3_state1.cube',0.07984014704791291]

ref_state1 = [ref_state1_hp1,ref_state1_hp2,ref_state1_hp3,ref_state1_hp4]
ref_group1 = [ref_state1]
list_ref_states.append(ref_group1)

ref_state2_hp1 = [orbdir+'NHO0_state2.cube',orbdir+'NPO0_state2.cube',0.984222214537887]
ref_state2_hp2 = [orbdir+'NHO1_state2.cube',orbdir+'NPO1_state2.cube',0.13742181537752118]
ref_state2_hp3 = [orbdir+'NHO2_state2.cube',orbdir+'NPO2_state2.cube',0.07945072673567238]
ref_state2_hp4 = [orbdir+'NHO3_state2.cube',orbdir+'NPO3_state2.cube',0.07816302891813448]

ref_state2 = [ref_state2_hp1,ref_state2_hp2,ref_state2_hp3,ref_state2_hp4]
ref_group2 = [ref_state2]
list_ref_states.append(ref_group2)

ref_state3_hp1 = [orbdir+'NHO0_state3.cube',orbdir+'NPO0_state3.cube',0.994238094821726]
ref_state3_hp2 = [orbdir+'NHO1_state3.cube',orbdir+'NPO1_state3.cube',0.063646035285663]
ref_state3_hp3 = [orbdir+'NHO2_state3.cube',orbdir+'NPO2_state3.cube',0.06292346055207389]
ref_state3_hp4 = [orbdir+'NHO3_state3.cube',orbdir+'NPO3_state3.cube',0.05899517869989282]

ref_state3 = [ref_state3_hp1,ref_state3_hp2,ref_state3_hp3,ref_state3_hp4]
ref_group3 = [ref_state3]
list_ref_states.append(ref_group3)

ref_state4_hp1 = [orbdir+'NHO0_state4.cube',orbdir+'NPO0_state4.cube',0.993934691603736]
ref_state4_hp2 = [orbdir+'NHO1_state4.cube',orbdir+'NPO1_state4.cube',0.057933397878477455]
ref_state4_hp3 = [orbdir+'NHO2_state4.cube',orbdir+'NPO2_state4.cube',0.05579232644687748]
ref_state4_hp4 = [orbdir+'NHO3_state4.cube',orbdir+'NPO3_state4.cube',0.05342841495066654]
ref_state4_hp5 = [orbdir+'NHO4_state4.cube',orbdir+'NPO4_state4.cube',0.05263241417933097]

ref_state4 = [ref_state4_hp1,ref_state4_hp2,ref_state4_hp3,ref_state4_hp4,ref_state4_hp5]
ref_group4 = [ref_state4]
list_ref_states.append(ref_group4)

ref_state5_hp1 = [orbdir+'NHO0_state5.cube',orbdir+'NPO0_state5.cube',0.996421834708167]
ref_state5_hp2 = [orbdir+'NHO1_state5.cube',orbdir+'NPO1_state5.cube',0.05986086145245728]
ref_state5_hp3 = [orbdir+'NHO2_state5.cube',orbdir+'NPO2_state5.cube',0.05966744994534111]

ref_state5 = [ref_state5_hp1,ref_state5_hp2,ref_state5_hp3]
ref_group5 = [ref_state5]
list_ref_states.append(ref_group5)

ref_state6_hp1 = [orbdir+'NHO0_state6.cube',orbdir+'NPO0_state6.cube',0.9999999999999999]

ref_state6 = [ref_state6_hp1]
ref_group6 = [ref_state6]
list_ref_states.append(ref_group6)

ref_state7_hp1 = [orbdir+'NHO0_state7.cube',orbdir+'NPO0_state7.cube',0.995811382168752]
ref_state7_hp2 = [orbdir+'NHO1_state7.cube',orbdir+'NPO1_state7.cube',0.09143134661132468]

ref_state7 = [ref_state7_hp1,ref_state7_hp2]
ref_group7 = [ref_state7]
list_ref_states.append(ref_group7)

ref_state8_hp1 = [orbdir+'NHO0_state8.cube',orbdir+'NPO0_state8.cube',0.9964861277333085]
ref_state8_hp2 = [orbdir+'NHO1_state8.cube',orbdir+'NPO1_state8.cube',0.08375796818856036]

ref_state8 = [ref_state8_hp1,ref_state8_hp2]
ref_group8 = [ref_state8]
list_ref_states.append(ref_group8)


gs_cfg = dict(
    enable=False,
    dir_R="/scratch/ekadashi/TEST_CODES/PhonExD/TEST_diabatization/R_c_CMOs/",
    dir_R0="/scratch/ekadashi/TEST_CODES/PhonExD/TEST_diabatization/R0_c_CMOs/",
    dir_R0_cmo="/scratch/ekadashi/TEST_CODES/PhonExD/TEST_diabatization/R0_c_CMOs/",
    occ_R=list(range(70, 81)),
    occ_R0=list(range(70, 81)),
    vir_R=list(range(81, 91)),
    vir_R0=list(range(81, 91)),
    occ_range=(70, 80),
    vir_range=(81, 90),
)

gs_cfg["orthogonalize_tildeh"] = True
gs_cfg["orth_method"] = "mgs"   # GS orthogonalization

small = 0.05
lwrite = False
#cp2k_output = '../SiH_4X4X1.out'
cp2k_output = '/scratch/ekadashi/TEST_CODES/PhonExD/TEST_diabatization/R_CMOs/SiH_4X4X1.out'
#Reference energy in hartree for all diagonal Hamiltonian elements
Eref = -144.43165222533139
#-144.431635233274051
list_group_diabs_start_ind = []
list_group_diabs_properties = []

#diabatize_states(list_adiabs,list_ref_states,cp2k_output,Eref,small,list_group_diabs_start_ind,list_group_diabs_properties,lwrite)
diabatize_states(list_adiabs,list_ref_states,cp2k_output,Eref,small,list_group_diabs_start_ind,list_group_diabs_properties,lwrite,gs_cfg=gs_cfg)

