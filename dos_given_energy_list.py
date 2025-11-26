import sys
from utils_holprt import *

data_file = sys.argv[1]
istart = int(sys.argv[2])
iend = int(sys.argv[3])

dos_given_energy_list(data_file,istart,iend)
