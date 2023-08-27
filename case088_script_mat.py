# -*- coding: utf-8 -*-
"""
Created on Thu May 25 14:03:54 2023

@author: taadebi2
"""

from qd.cae.dyna import *
import os


# loop for changing the young modulus of one rod at a time from the default file 
# (i.e., every change starts from the default file)

Keyword.name_alignment = Keyword.align.right
Keyword.field_alignment = Keyword.align.right 


for i in range(9,109):
    kf = KeyFile("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/FA_simp_88GPa_rods_qd_final.K") # keyword file from the Case088_script
    mat = kf["*MAT_ELASTIC_TITLE"]
    print(mat[i])
    mat[i].set_card_valueByName("e", 23.0)
    mat[i].reformat_all()
    os.makedirs("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/Rods_KF_Final/Er" + str(i-8) + "-23GPa") # make directory for each case
    kf.save("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/Rods_KF_Final/Er" + str(i-8) + "-23GPa/Er" + str(i-8) + "-23GPa.K") # save keyword