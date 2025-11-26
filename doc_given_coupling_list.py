import sys
from utils_holprt import *

data_file = sys.argv[1]
istart_bra = int(sys.argv[2])
iend_bra = int(sys.argv[3])
istart_ket = int(sys.argv[4])
iend_ket = int(sys.argv[5])
labs = False
labs_text = sys.argv[6]
if labs_text == 'True':
    labs = True

list_bra = []
#istart = 0
#iend = 5
for i in range(istart_bra,iend_bra+1):
    list_bra.append(i)

list_ket = []
#jstart = 0
#jend = 5
for j in range(istart_ket,iend_ket+1):
    list_ket.append(j)

list_pairs = []
#list_pairs.append([0,12])
#list_pairs.append([0,22])
#list_pairs.append([1,13])
#list_pairs.append([1,23])
#list_pairs.append([2,12])
#list_pairs.append([2,14])
#list_pairs.append([2,22])
#list_pairs.append([2,24])
#list_pairs.append([3,13])
#list_pairs.append([3,15])
#list_pairs.append([3,23])
#list_pairs.append([3,25])
#list_pairs.append([4,14])
#list_pairs.append([4,16])
#list_pairs.append([4,24])
#list_pairs.append([4,26])
#list_pairs.append([5,15])
#list_pairs.append([5,17])
#list_pairs.append([5,25])
#list_pairs.append([5,27])
#list_pairs.append([6,16])
#list_pairs.append([6,18])
#list_pairs.append([6,26])
#list_pairs.append([6,28])
#list_pairs.append([7,17])
#list_pairs.append([7,19])
#list_pairs.append([7,27])
#list_pairs.append([7,29])
#list_pairs.append([8,18])
#list_pairs.append([8,20])
#list_pairs.append([8,28])
#list_pairs.append([8,30])
#list_pairs.append([9,19])
#list_pairs.append([9,21])
#list_pairs.append([9,29])
#list_pairs.append([9,31])
#list_pairs.append([10,20])
#list_pairs.append([10,30])
#list_pairs.append([11,21])
#list_pairs.append([11,31])

doc_given_coupling_list(data_file,list_bra,list_ket,list_pairs,labs=labs,small=0.001)
