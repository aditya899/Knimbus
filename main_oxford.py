import csv

with open('knimbus_oxford.csv') as csv_record:
    reader = csv.DictReader(csv_record)
    for i,row in enumerate(reader):
        print(str(i+1)+".")
        print("Title:- "+row['TITLE']+"\n"+"Link:- "+row['LINK']+"\n"+"Year:- "+row['YEAR']+"\n"+"Authors:- "+row['AUTHOR'])
        if(i>=9):
            break
