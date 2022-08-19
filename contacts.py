
# python program reads google contacts csv file and extracting only 
# name, address, email & main phone number.
# The program makes the following assumptions:
# The input file comes from Google contacts with a download of the name
# "contacts.csv" in comma separated variable (CSV) format.
# The output file is called contactsOut.csv .
# Edit contactsOut.csv: Line 1 needs to be edited to be the desired column
# headings. Tab separated. The file is then imported back into a google sheets
# document, the column separator "Tab" is selected. When the import into the 
# spreadsheet is complete is complete
# set column widths and justification as desired. Export again as a pdf. It
# It can be found in the download folder as contactsOut.pdf

import csv
# open output file
Contacts2 = open(r"C:\Users\mark\Downloads\Downloads\contactsOut.csv", "w")
# open input file
with open(r"C:\Users\mark\Downloads\Downloads\contacts.csv", "r") as csvfile:
    #the csv.reader function is defined in the csv package
    contacts = csv.reader(csvfile, delimiter = ',')
    for row in contacts:
                print(row[3]+", "+row[1],",",row[30], ",",row[36])
                Contact2str=(row[3]+", "+row[1]+"\t"+row[30]+"\t"+row[36]+"\n")
                Contacts2.write(Contact2str)
Contacts2.close()
