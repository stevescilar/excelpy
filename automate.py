from openpyxl import Workbook, load_workbook

wb = load_workbook('marks.xlsx')
ws = wb.active
print(ws)
