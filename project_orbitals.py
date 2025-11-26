import sys
from utils_holprt import *


list_orb_to_proj = ['VBM_G_layer1_0.cube','VBM_G_layer1_1.cube']
list_orb_proj_to = ['VBM_G_layer1_antisym_220_ref.cube']
n_collect = 2

lwrite = True

proj_orbs(list_orb_to_proj,list_orb_proj_to,n_collect,[],[],lwrite)
