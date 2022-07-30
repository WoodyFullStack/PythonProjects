import openpyxl

book_path = "inventory.xlsx"
book = openpyxl.load_workbook(book_path)
sheet = book.active
max_row = sheet.max_row
max_column = sheet.max_column

# How many products each company have - new company can be added to Excel - it will count. Not only 3.
company_list = []
company_list_count = []
result = {}

for x in range(2, max_row+1):
    company_list.append(sheet.cell(x, 4).value)
company_list_unique = list(set(company_list))
for x in company_list_unique:
    counter = 0
    for y in company_list:
        if y == x:
            counter = counter+1
    company_list_count.append(counter)
for x in range(0, len(company_list_unique)):
    result[company_list_unique[x]] = company_list_count[x]
print(result)

# how many products with Inventory less 10
invent_less_than = {}
for x in range(2, max_row+1):
    if sheet.cell(x, 2).value < 10:
        invent_less_than[sheet.cell(x, 1).value] = sheet.cell(x, 2).value
print(invent_less_than)

# Inventory value of each company
company_list_value = []
for company in company_list_unique:
    counter = 0
    for x in range(2, max_row+1):
        if sheet.cell(x, 4).value == company:
            counter = counter + (sheet.cell(x, 2)).value * (sheet.cell(x, 3)).value
    company_list_value.append(counter)
for x in range(0, len(company_list_unique)):
    result[company_list_unique[x]] = company_list_value[x]
print(result)

# Write Value for each product
sheet.cell(1, max_column + 1).value = "Product value"
for x in range(2, max_row+1):
    sheet.cell(x, max_column + 1).value = (sheet.cell(x, 2)).value * (sheet.cell(x, 3)).value
book.save("inventory2.xlsx")
