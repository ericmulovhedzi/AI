
# File: excel_csv_export.py
# Author: Eric Mulovhedzi
# Created on March 15, 2021, 12:36 PM
# A script to convert all the excel documents for both file extensions ".xlsm" and ".xlsx" using panda library

# importing packadges 

import warnings
import pandas as pd 
import os

class Spreadsheet:

    def __init__(self, directory, separator):
        self.directory = directory
        self.separator = separator

    def __str__(self):
    	return f"Folder name is '{self.directory}', separator is '{self.separator}'."
    
    def __repr__(self):
    	return f"{self.directory}ToCSV('{self.separator}')"
    
    def convert_excel_to_csv(self):# Excel to CSV conversion function
    	warnings.simplefilter(action='ignore', category=UserWarning)
    	for filename in os.scandir(self.directory):
    		if filename.is_file():
    			fl = "F: "+filename.path
    		else:
    			print("D: "+filename.path)
    			if not os.path.exists(filename.path+"/CSV"):
    				os.mkdir(filename.path+"/CSV")
    			for excl in os.scandir(filename.path):
    				if excl.is_file():
    					if (excl.path.endswith('.xlsm') or excl.path.endswith('.xlsx')):
    						file_ = os.path.splitext(os.path.basename(excl.path))[0]
    						print("   DIRECTORY: "+excl.path)
    						read_file = pd.read_excel(excl.path)
    						read_file.to_csv (filename.path+"/CSV/"+file_+".csv", sep = self.separator,index = None, header=True)
    						
    	print("Excel to CSV conversion complete!")

Excel = Spreadsheet("excel",";") # Declare and initialise a Spreadsheet class to look for MS Excel documents inside a folder named "excel" and separate the CSV files using "|" as a delimeter

print(str(Excel))
print(repr(Excel))

Excel.convert_excel_to_csv() # Convert Excel files to CSV
