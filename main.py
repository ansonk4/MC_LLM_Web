import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns(3)

recurment = col1.container(border=True)
recurment.write(f'臨時招募')
six = recurment.number_input('六星 (+50分)', step = 1)
five = recurment.number_input('五星 (+20分)', step = 1)
four = recurment.number_input('四星 (+10分)', step = 1)
rec_tol = six*50 + five*20 + four*10
recurment.subheader(rec_tol)

ending = col1.container(border = True)
ending.write('結局')
end1 = ending.checkbox('息潮的代價 (+80分)')
end2 = ending.checkbox('靜謐時代 (+350分)')
end_score = end1*80 + end2*350 
ending.subheader(end_score)

secret_floor = col1.container(border = True)
secret_floor.write('誤入奇境')
floor = secret_floor.radio('floor', ['未完成 (+0分)', '荒地群獵-銹錘 (+120分)', '寒災之咒-寒災 (+150分)', '險路勿近-墓碑 (+230分)'], label_visibility='collapsed')
floor_to_score = {'未完成 (+0分)': 0, '荒地群獵-銹錘 (+120分)': 120, '寒災之咒-寒災 (+150分)': 150, '險路勿近-墓碑 (+230分)': 230}
floor_score = floor_to_score[floor]
secret_floor.subheader(floor_score)


emergency = col2.container(border=True)
emergency.write('緊急作戰')
e_3 = emergency.expander('第三層')
e_3_1 = e_3.number_input('巢穴 (+40分)', step = 1)
e_3_2 = e_3.number_input('大君遺脈 (+40分)', step = 1)
e_3_3 = e_3.number_input('漩渦(有騎士且存活時) (+40分)', step = 1)
e_3_4 = e_3.number_input('据險固守 (+40分)', step = 1)

e_4 = emergency.expander('第四層')
e_4_1 = e_4.number_input('海窟沙暴(無漏時) (+50分)', step = 1)
e_4_2 = e_4.number_input('溟痕樂園(無漏時) (+50分)', step = 1)
e_4_3 = e_4.number_input('狩獵場 (+60分)', step = 1)
e_4_4 = e_4.number_input('領地意識 (+100分)', step = 1)

e_5 = emergency.expander('第五層')
e_5_1 = e_5.number_input('機械之災 (+50分)', step = 1)
e_5_2 = e_5.number_input('好夢在何方 (+50分)', step = 1)
e_5_3 = e_5.number_input('育生池 (+60分)', step = 1)
e_5_4 = e_5.number_input('失控 (+100分)', step = 1)

e_6 = emergency.expander('第六層')
e_6_1 = e_6.number_input('深度認知 (+90分)', step = 1)
e_6_2 = e_6.number_input('水火相容 (+150分)', step = 1)

emergency_score = (e_3_1 + e_3_2 + e_3_3 + e_3_4) * 40 + e_4_1 * 50 + e_4_2 * 50 + e_4_3 * 60 + e_4_4 * 100 \
  + e_5_1 * 50 + e_5_2 * 50 + e_5_3 * 60 + e_5_4 * 60 + e_6_1 * 90 + e_6_2 * 150
emergency.subheader(emergency_score)

duck = col3.container(border = True)
duck.write('鴨爵與雇員')
duck1 = duck.checkbox('鴨本運作 (+80分)')
duck_score = duck1 * 80
duck.subheader(duck_score)


challenge = col3.container(border = True)
challenge.write('特殊挑戰')
c_1 = challenge.checkbox('真相 (+50分)')
c_2 = challenge.checkbox('真相(無漏) (+90分)')
c_3 = challenge.checkbox('”喜”從箱來 (+50分)')
c_4 = challenge.checkbox('”喜”從箱來(無漏+箱子全收) (+90分)')
c_5 = challenge.checkbox('狂信如火(無漏時) (+50分)')
c_total = c_1 * 50 + c_2 * 90 + c_3 * 50 + c_4 * 90 + c_5 * 50
challenge.subheader(c_total)


enemy = col3.container(border = True)
enemy.write('隱藏敵人')
en = enemy.number_input('擊殺鴨爵，高普尼克，流淚小子 (+20分)', step = 1)
en_score = en * 20
enemy.subheader(en_score)

mis = col3.container(border = True)
collectibles = mis.number_input('藏品 (+10分)', step = 1)
enlightenment = mis.number_input('啓示 (+50分)', step = 1)
mis_score = collectibles * 10 + enlightenment * 50
mis.subheader(mis_score)

total_score = rec_tol + end_score + floor_score + emergency_score + duck_score + c_total + en_score + mis_score
st.metric('總分', value=total_score)