import openpyxl

wk = openpyxl.Workbook()
sh = wk.active
sh.title = "Test"

print(sh.title)

sh['A3'].value="test,com"

#2nd Sheet is created
wk.create_sheet(title="TestingW")
sh1 = wk['TestingW']
sh1['A6']='67896544332455'

#saving
wk.save('C:\\Users\\lts\\Documents\\Book2.xlsx' )

