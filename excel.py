from openpyxl.workbook import Workbook
from openpyxl import load_workbook

# create a workbook object

wb = Workbook()

# create an active worksheet
ws = wb.active

# load existing excel sheet

wb = load_workbook('marks.xlsx')