# library for reading data and formatting information from an excel file
import xlrd

# specifying the location of the excel file
file_location = "C:/Users/Brian/Desktop/Data returned for visualisation"
workbook = xlrd.open_workbook(file_location)


sheet = workbook.sheet_by_index(0)
sheet.cell_value(0, 0) # reading first value from spreadsheet

# reading from a row
sheet.nrows

# reading from a column
sheet.ncols

# reading a specific row
for col in range (sheet.ncols):
    sheet.cell_value(0, col)

