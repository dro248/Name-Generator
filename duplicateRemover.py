import csv
import sys

names = set()

#import names
with open(sys.argv[1], 'rU') as csvfile:
	csvreader = csv.reader(csvfile, dialect=csv.excel_tab)
	for row in csvreader:
		names.add(row[0])

#write no dupes file
with open('noDuplicates.csv', 'wb') as outfile:
	for item in names:
		outfile.write(item + "\n")