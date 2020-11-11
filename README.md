# ColdNutritionTracker
This is a simple Python script that works with google sheets in order to feel up you calories intake sheet.

## How to run ths script
1. Prepare a google sheets as in Image1 and Image2.
2. Make formulas to summ your macros in the top as in Image1 head section. Make formulas as in Image2 to count your macros of the products per weight.
3. Download Google API and go through a Google Sheets API setup for Pyethon using https://developers.google.com/sheets/api/quickstart/python
4. When you've got file creds.json in your folder, download file ColdNutritionTracker.py from repository.
5. Import all libraries at the top of the code using pip or settings in PyCharm.
5. Change SpreadsheetId and other unique information.
6. Change the range, cells or command to your personal requirements.
  
 ## How to use script
 1. Make a cell range in the table with dates, that you are going to fill.
 2. After running script fill the date, product and weight.
 3. Check if the sheet is updated
 
 ## Dependencies
 - Python
 - Google sheets API
