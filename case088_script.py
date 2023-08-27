# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:57:23 2023

@author: taadebi2
"""

from qd.cae.dyna import *

# accessing the keyword file
kf = KeyFile("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/FA_simp_88GPa_rods.K")
print(kf.keys())

# accessing all in the part ID (returns a list)
part = kf["*PART"]

#initalization
part_step = range(10,109)
section_id = range(21,121)
mat_id = range(112,212)

# initializing the keyword for right alignment (default is left alignment)
Keyword.name_alignment = Keyword.align.right
Keyword.field_alignment = Keyword.align.right 

# Linking section id and material id with part id

for i in part_step:
    part[i].set_card_valueByName("e", 230)
    
for i,j,k in zip(part_step, section_id, mat_id): 
    part[i].set_card_valueByName("secid", j)
    part[i].set_card_valueByName("mid", k)
    part[i].reformat_all()
    #print(part[i])
kf.save("C:/Users/taadebi2/Desktop/LS_DYNA_Projects/simplified_FA/case088/case088/FA_simp_88GPa_rods_qd_edit.K")



mat_step = range(10,109)



