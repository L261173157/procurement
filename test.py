import xlrd
from datetime import date,datetime
def read_excel():
    workbook=xlrd.open_workbook("E:\Python\caigou.xlsx")
    sheet1_name = workbook.sheet_names()[0]
    print(sheet1_name)
    sheet1=workbook.sheet_by_index(0)
    print(sheet1.cell(1,2).value)
read_excel()


