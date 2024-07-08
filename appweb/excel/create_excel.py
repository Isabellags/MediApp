import openpyxl

excel_book=openpyxl.Workbook()
sheet=excel_book.active

data= [
    ("Name", "Age", "Company"),
    ("Isabella", "35", "Google"),
    ("Stephania", "40", "Amazon"),
    ("Luis", "30", "Github"),
    ("Susan", "45", "Visual"),
]

for index,row in enumerate(data):
    sheet[f'A{index+1}'] = row[0]
    sheet[f'B{index+1}'] = row[1]
    sheet[f'C{index+1}'] = row[2]

excel_book.save("my_excel_file.xlsx")    