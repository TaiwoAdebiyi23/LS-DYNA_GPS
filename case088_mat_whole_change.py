# -*- coding: utf-8 -*-
"""
Created on Mon May 29 13:58:10 2023

@author: taadebi2
"""

from qd.cae.dyna import *
import os


kf = KeyFile("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/FA_simp_88GPa_rods_qd.K") # keyword file from the Case088_script
mat = kf["*MAT_ELASTIC_TITLE"]

Keyword.name_alignment = Keyword.align.right
Keyword.field_alignment = Keyword.align.right 

for i in range(2,8):
    print(mat[i])
    mat[i].set_card_valueByName("pr",0.34)
    mat[i].reformat_all()
    
    
for i in range(9,109):
    print(mat[i])
    mat[i].set_card_valueByName("e",230)
    mat[i].set_card_valueByName("pr",0.32)
    mat[i].set_card_valueByName("ro",1.09600E-5)
    mat[i].reformat_all()
    
kf.save("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/FA_simp_88GPa_rods_qd_final.K") # save keyword