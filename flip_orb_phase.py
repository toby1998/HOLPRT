import sys
from utils_holprt import *

input_filnam = sys.argv[1]
truncate = input_filnam.split('.cube')[0]
output_filnam = truncate + '_rephase.cube'
print(output_filnam)

if not file_exists(input_filnam):
    print(f'{input_filnam} does not exit. Bombing out!')
    sys.exit()

if file_exists(output_filnam):
    print(f'Warning! {output_filnam} exists. Do you want to overwrite?')
    user_input = input("Please enter Y/y to continue: ")
    if user_input != 'Y' and user_input != 'y': sys.exit()

flip_phase_orbcube(input_filnam,output_filnam)
