import streamlit as st
import pandas as pd

total_score = 0

st.metric('Total Score', value=total_score)

col1, col2, col3 = st.columns(3)

recurment = col1.container(border=True)
recurment.write(f'臨時招募')
six = recurment.number_input('六星 (+50分)', step = 1)
five = recurment.number_input('五星 (+20分)', step = 1)
four = recurment.number_input('四星 (+10分)', step = 1)
rec_tol = six*50 + five*20 + four*10
recurment.write(rec_tol)

ending = col1.container(border = True)
ending.write('結局')
end = ending.radio('結局',['未完成 (+0分)', '息潮的代價 (+80分)', '命運的寵兒 (+350分)', '靜謐時代 (+350分)'])
end_to_score = {'未完成 (+0分)': 0, '命運的寵兒 (+350分)': 350, '靜謐時代 (+350分)': 350, '息潮的代價 (+80分)': 80}
end_score = end_to_score[end]
ending.write(end_score)

secret_floor = col1.container(border = True)
secret_floor.write('誤入奇境')
floor1 = secret_floor.checkbox('荒地群獵-銹錘 (+120分)')
floor2 = secret_floor.checkbox('寒災之咒-寒災 (+150分)')
floor3 = secret_floor.checkbox('險路勿近-墓碑 (+230分)')
floor_score = floor1*120 + floor2*150 + floor3*230
secret_floor.write(floor_score)


#【緊急作戰】方面，
# 第三層緊急: 巢穴+40分，大君遺脈+40分，漩渦(有騎士且存活時)+40，
# 第四層緊急：領地意識+100分，狩獵場+60分，溟痕樂園(無漏時)+50分，海窟沙暴(無漏時)+50分
# 第五層緊急：失控+150分，育生池+90分，好夢在何方+90分，機械之災+60分
# 第六層緊急：水火相容+150分，深度認知+90分
# 誤入奇境遇到對應關卡也計算分數。
# 漏護盾血也算漏。

emergency = col2.container(border=True)
emergency.write('緊急作戰')
emergency.write('第三層')
e_3_1 = emergency.number_input('巢穴 (+40分)', step = 1)
e_3_2 = emergency.number_input('大君遺脈 (+40分)', step = 1)
e_3_3 = emergency.number_input('漩渦(有騎士且存活時) (+40分)', step = 1)

emergency.write('第四層')
e_4_1 = emergency.number_input('海窟沙暴(無漏時) (+50分)', step = 1)
e_4_2 = emergency.number_input('溟痕樂園(無漏時) (+50分)', step = 1)
e_4_3 = emergency.number_input('狩獵場 (+60分)', step = 1)
e_4_4 = emergency.number_input('領地意識 (+100分)', step = 1)

emergency.write('第五層')
e_5_1 = emergency.number_input('機械之災 (+50分)', step = 1)
e_5_2 = emergency.number_input('好夢在何方 (+50分)', step = 1)
e_5_3 = emergency.number_input('育生池 (+60分)', step = 1)
e_5_4 = emergency.number_input('失控 (+100分)', step = 1)
