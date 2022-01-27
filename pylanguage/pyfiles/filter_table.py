import pandas as pd
import re
import copy
import openpyxl
import random

ss = pd.read_excel("C:\\Downloads\\07.01_1.xlsx", sheet_name="Sheet1")
#Find in column information about employees
ss = ss.loc[ss['Результат'] != "Не обнаружено"]
ss2 = ss.loc[:]
ss2.insert(19, "Уволен", "-")
ss2.insert(1, "Рег", "$")
for i in ss2.index:
	if re.search(r'.{0,}не.{0,}', str(ss2.at[i, 'Статус сотрудника']), flags=re.IGNORECASE):
		ss2.at[i, 'Уволен'] = 'НЕТ'
	elif (re.search(r'[ ]{0,}да[ ]{0,}', str(ss2.at[i, 'Статус сотрудника']), flags=re.IGNORECASE)):
		ss2.at[i, 'Уволен'] = 'ДА'
	ss2.at[i, 'Рег'] = re.sub(r'L([0-9]{0,})([A-Z])0{0,}([0-9]{0,})', r'^L\1\2\3$', str(ss2.at[i, 'ФИО']))
writer = pd.ExcelWriter("C:\\Downloads\\07.01_1_formate.xlsx", engine='xlsxwriter')
ss2.to_excel(writer, sheet_name='Sheet1')
#Highlight duplicates
wb = writer.book
ws = writer.sheets['Sheet1']
format1 = wb.add_format({'bg_color': '#FFC7CE',
                               'font_color': '#9C0006'})
format2 = wb.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})
format3 = wb.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})				   
st_row = 1
st_col = 3
e_row = len(ss2)
e_col = st_col
l = pd.unique(ss2['ФИО'])
f = [format1, format2, format3]
i = 0
while i < len(l):
	ws.conditional_format(st_row, st_col, e_row, e_col,
								{'type':     'text',
								'criteria': 'containing',
								'value':    l[i],
								'format':   f[i % 3]})
	i += 1
writer.save()