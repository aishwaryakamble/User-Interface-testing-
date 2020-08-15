import openpyxl

wb = openpyxl.Workbook()

wb.create_sheet('testing',0)	


sheet = wb['testing']
cell = sheet['A2']
cell.value = '2'
print(cell.value)

wb.save('testing.xlsx')