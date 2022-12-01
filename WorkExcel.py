import openpyxl #Устанавите перед работой openpyxl

# чтение excel-файла
wb = openpyxl.load_workbook('test_exc.xlsx')

# печать списка листов
sheets = wb.sheetnames
for sheet in sheets:
    print(sheet)

# получаем выбранный лист
sheet = wb.active

# печатаем значение ячейки A1(для примера)
print(sheet['A1'].value)
# печатаем значение ячейки B1
print(sheet['B1'].value)